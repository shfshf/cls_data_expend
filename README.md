## 提取语料中的句式，分别针对不同的实体类型扩展相应的语料

## data
* data/raw 中初始的横向的少量数据集data.json
* mapping.json 是一个字典，分别为需要扩展的实体名与对应的实体列表名
* data/dict 人物_企业家国内.json, 城市.json等json文件是需要扩展实体的list
* configure.json 是文件与超参数配置，
  其中max_list_expend是data实体list扩展的限度，低于限度的实体全部保留，超过限度的实体数量：按照限度阈值随机抽取限度数量的个数进行扩展

## code
### 对初始的语料根据实体列表进行扩展

* meta_generate.py 将 data/dict 中所有的实体list 提取成需要扩展的 k,v 字典格式，保存为meta.json文件
* json_to_conllx.py 将初始的json格式的语料转换成 conllx 格式语料
* generate_seq.py 读取生成的 data.conllx 语料，根据mapping.json字典映射表，寻找data文件夹里面需要扩展的实体list进行语料扩充

all_run_expend.py 顺序执行上面的三个脚本, 生成的扩展后的语料保存在'./data/expend/data_expend.conllx'

