#    Copyright 2020 Division of Medical Image Computing, German Cancer Research Center (DKFZ), Heidelberg, Germany
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


import torch
from tuframework.training.network_training.tuTrainerV2 import tuframeworkTrainerV2


class tuframeworkTrainerV2_Adam(tuframeworkTrainerV2):

    def initialize_optimizer_and_scheduler(self):
        self.optimizer = torch.optim.Adam(self.network.parameters(), self.initial_lr, weight_decay=self.weight_decay, amsgrad=True)
        self.lr_scheduler = None


tuframeworkTrainerV2_Adam_copy1 = tuframeworkTrainerV2_Adam
tuframeworkTrainerV2_Adam_copy2 = tuframeworkTrainerV2_Adam
tuframeworkTrainerV2_Adam_copy3 = tuframeworkTrainerV2_Adam
tuframeworkTrainerV2_Adam_copy4 = tuframeworkTrainerV2_Adam
