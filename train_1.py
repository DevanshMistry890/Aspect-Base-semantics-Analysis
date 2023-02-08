from pyabsa import AspectTermExtraction as ATEPC

config = ATEPC.ATEPCConfigManager.get_atepc_config_chinese()
config.model = ATEPC.ATEPCModelList.FAST_LCF_ATEPC
config.evaluate_begin = 0
config.max_seq_len = 256
config.batch_size = 8
# config.pretrained_bert = 'yangheng/deberta-v3-base-absa'
config.pretrained_bert = "microsoft/deberta-v3-base"
config.log_step = -1
config.l2reg = 1e-8
config.num_epoch = 20
config.seed = 42
config.use_bert_spc = True
config.use_amp = False
config.cache_dataset = True
config.cross_validate_fold = -1

chinese_sets = ATEPC.ATEPCDatasetList.Multilingual

aspect_extractor = ATEPC.ATEPCTrainer(
    config=config,
    from_checkpoint="",
    dataset=chinese_sets,
    checkpoint_save_mode=1,
    auto_device=True,
    load_aug=True,
).load_trained_model()

atepc_examples = [
    "But the staff was so nice to us .",
    "But the staff was so horrible to us .",
    r"Not only was the food outstanding , but the little ` perks \' were great .",
    "It took half an hour to get our check , which was perfect since we could sit , have drinks and talk !",
    "It was pleasantly uncrowded , the service was delightful , the garden adorable , "
    "the food -LRB- from appetizers to entrees -RRB- was delectable .",
    "How pretentious and inappropriate for MJ Grill to claim that it provides power lunch and dinners !",
]
aspect_extractor.batch_predict(
    target_file_or_examples=atepc_examples,  #
    save_result=True,
    print_result=True,  # print the result
    pred_sentiment=True,  # Predict the sentiment of extracted aspect terms
)