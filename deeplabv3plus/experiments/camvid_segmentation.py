import os
import wandb
from glob import glob
from ..train import Trainer, tf


def run_training():
    config = {
        'wandb_api_key': '60cfb770bc5de44f181c8cb5e270eb266bc918c6',
        'project_name': 'deeplabv3-plus',
        'experiment_name': 'camvid-segmentation-resnet-50-backbone',
        'train_dataset_configs': {
            'images': sorted(glob('./dataset/camvid/train/*')),
            'labels': sorted(glob('./dataset/camvid/trainannot/*')),
            'height': 512, 'width': 512, 'batch_size': 8
        },
        'val_dataset_configs': {
            'images': sorted(glob('./dataset/camvid/val/*')),
            'labels': sorted(glob('./dataset/camvid/valannot/*')),
            'height': 512, 'width': 512, 'batch_size': 8
        },
        'strategy': tf.distribute.OneDeviceStrategy(device="/gpu:0"),
        'num_classes': 12, 'height': 512, 'width': 512,
        'backbone': 'resnet50', 'learning_rate': 0.0001,
        'checkpoint_path': os.path.join(
            './checkpoints',
            'deeplabv3-plus-camvid-segmentation-resnet-50-backbone.h5'
        ),
        'epochs': 100
    }
    trainer = Trainer(config)
    trainer.connect_wandb()
    history = trainer.train()
    return history
