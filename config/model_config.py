from model.roberta_classifier import RobertaClassifier
from model.bert_classifier import BertClassifier
from model.roberta_classifier_large import RobertaClassifierL
# from model.roberta_classifier_qa import RobertaClassifierQA
from model.longformer_classifier import LongformerClassifier
from model.lstm_classifier import LSTMClassifier
from model.sklearn_classifier import RandomForestSKLearnClassifier, LogisticRegressionSKLearnClassifier

# model_dict = {'model': ["lstm"]}
# model_dict = {'model': ["random_forest", "logistic_regression"]}
model_dict = {'model': ["roberta_large"]}
# model_dict = {'model': ["roberta"]}
# model_dict = {'model': ["longformer"]}

model_info = {
	'bert': {
		'class': BertClassifier,
		"tunable_model_args": {
			# "hidden_dropout_prob": [0.1, 0.2, 0.3]
			"hidden_dropout_prob": [0.1]
		}
	},
	'roberta': {
		'class': RobertaClassifier,
		"tunable_model_args": {
			# "hidden_dropout_prob": [0.1, 0.2, 0.3]
			"hidden_dropout_prob": [0.1]
		}
	},
	'roberta_large': {
		'class': RobertaClassifierL,
		"tunable_model_args": {
			"hidden_dropout_prob": [0.1]
		}
	},
	# 'roberta_qa': {
	# 	'class': RobertaClassifierQA,
	# 	"tunable_model_args": {
	# 		"hidden_dropout_prob": [0.1]
	# 	}
	# },
	'longformer': {
		'class': LongformerClassifier,
		"tunable_model_args": {
			"hidden_dropout_prob": [0.1]
		}
	},
	"lstm": {
		"class": LSTMClassifier,
		"tunable_model_args": {
			"hidden_size": [100,200,300],
			"pad_packing": True,
		}
	},
	"random_forest": {
		"class": RandomForestSKLearnClassifier,
		"tunable_model_args": {
			'n_estimators': [4, 16, 64, 256, 512]
		}
	},
	"logistic_regression": {
		"class": LogisticRegressionSKLearnClassifier,
		"tunable_model_args": {
			'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]
		}
	}
}
