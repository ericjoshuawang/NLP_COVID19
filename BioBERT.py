'''
CUDA_VISIBLE_DEVICES=0,1,2,3 python run_qa.py --do_train=True --do_predict=True --vocab_file=$BIOBERT_DIR/vocab.txt --bert_config_file=$BIOBERT_DIR/bert_config.json --init_checkpoint=$BIOBERT_DIR/model.ckpt-1000000 --max_seq_length=384 --train_batch_size=6 --learning_rate=5e-6 --doc_stride=128 --num_train_epochs=5.0 --do_lower_case=False --train_file=$QA_DIR/BioASQ-train-factoid-4b.json --predict_file=$QA_DIR/BioASQ-test-factoid-4b-1.json --output_dir=$OUTPUT_DIR

java -Xmx10G -cp $CLASSPATH:./flat/BioASQEvaluation/dist/BioASQEvaluation.jar evaluation.EvaluatorTask1b -phaseB -e 5 4B1_golden.json BioASQform_BioASQ-answer.json

CUDA_VISIBLE_DEVICES=0,1,2,3 python run_qa.py --do_train=True --do_predict=True --vocab_file=$BIOBERT_DIR/vocab.txt --bert_config_file=$BIOBERT_DIR/bert_config.json --init_checkpoint=$BIOBERT_DIR/model.ckpt-14599 --max_seq_length=384 --train_batch_size=1 --learning_rate=5e-6 --doc_stride=128 --num_train_epochs=5.0 --do_lower_case=False --train_file=$QA_DIR/BioASQ-train-factoid-4b.json --predict_file=$QA_DIR/BioASQ-test-factoid-4b-1.json --output_dir=$OUTPUT_DIR
'''