import argparse
from deepsegment import DeepSegment
from deepcorrect import DeepCorrect


def parse_args():
    parser = argparse.ArgumentParser(description='Add punctuation to the file')
    parser.add_argument('--input', help='path to input text file', type=str)
    parser.add_argument('--params_path', help='path to parameters file', type=str)
    parser.add_argument('--checkpoint_path', help='path to checkpoint', type=str)
    parser.add_argument('--output', help='path to output text file', type=str)
    args = parser.parse_args()
    return args


def main():

    args = parse_args()

    with open(args.input, mode='r') as read_text_file:
        line = read_text_file.readline()

        segmenter = DeepSegment('en')
        corrector = DeepCorrect(args.params_path, args.checkpoint_path)

    with open(args.output, mode='w') as close_text_file:
        for part in segmenter.segment(line):
            tester2 = corrector.correct(part)
            close_text_file.write(tester2[0]['sequence'] + '\n')


if __name__ == '__main__':
    main()
