#!/usr/bin/env bash

CUB_ENCODER=lm_sje_nc4_cub_hybrid_gru18_a1_c512_0.00070_1_10_trainvalids.txt_iter30000.t7 \
CAPTION_PATH=Data/birds/example_captions \
GPU=0 \

export CUDA_VISIBLE_DEVICES=${GPU}

#
# Speech-To-Text
#
deepspeech --model deepspeech-0.5.0-models/output_graph.pbmm \
--alphabet deepspeech-0.5.0-models/alphabet.txt \
--lm deepspeech-0.5.0-models/lm.binary \
--trie deepspeech-0.5.0-models/trie \
--audio audio/birds_example.wav \
--outfile ${CAPTION_PATH}.txt

#
# Extract text embeddings from the encoder
#
net_txt=text_encoder/${CUB_ENCODER} \
queries=${CAPTION_PATH}.txt \
filenames=${CAPTION_PATH}.t7 \
th get_embedding.lua

#
# Generate image from text embeddings
#
python3 demo.py \
--cfg cfg/birds-demo.yml \
--gpu ${GPU} \
--caption_path ${CAPTION_PATH}.t7
