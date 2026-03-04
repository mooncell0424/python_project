python data_multi30k.py --pair_dir $1 --dest_dir $1 --src_lang $2 --trg_lang $3

# 新建train_l文件，合并两个文件到一个文件
touch $1/train_l
cat $1/train_src.cut.txt >> $1/train_l
cat $1/train_trg.cut.txt >> $1/train_l

# 生成词表，subword方式,统一用10000个subword
subword-nmt learn-joint-bpe-and-vocab \
    -i $1/train_l \  # 输入文件
    -s 10000 \  # 生成10000个subword
    -o $1/bpe.10000 \  # 输出bpe文件
    --write-vocabulary $1/vocab # 输出词表文件，包含所有的subword和原始词汇

# 应用分词
for mode in train val test; do
    subword-nmt apply-bpe -c $1/bpe.10000 < $1/${mode}_src.cut.txt > $1/${mode}_src.bpe
    subword-nmt apply-bpe -c $1/bpe.10000 < $1/${mode}_trg.cut.txt > $1/${mode}_trg.bpe
    echo "Finished applying bpe to ${mode} files."
done
