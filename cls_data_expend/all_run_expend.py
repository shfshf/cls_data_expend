import os

# os.system("python -m data_expend.dict_to_json")
os.system("python -m cls_data_expend.meta_generator")
os.system("python -m cls_data_expend.json_to_conllx")
os.system("python -m data_expend.merge_data")
os.system("python -m cls_data_expend.generate_seq2")
