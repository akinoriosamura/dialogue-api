#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from parlai.core.agents import create_agent
from parlai.core.worlds import create_task
from parlai.core.params import ParlaiParser
import parlai.chat_service.utils.config as config_utils
from parlai.core.opt import Opt
from parlai.agents.safe_local_human.safe_local_human import SafeLocalHumanAgent

import json
import os


class ParlAI(object):
    def __init__(self):
        self.SHARED = {}
        self.parlai_home = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'ParlAI')
        self.parlai_datapath = os.path.join(self.parlai_home, 'data')
        self.parlai_download = os.path.join(self.parlai_home, 'downloads')
        self.opt = self.setup_opt()
        self.setup_interactive()

    def setup_opt(self):
        opt = Opt()
        config_path = '/app/src/nlp/config.yml'
        config = config_utils.parse_configuration_file(config_path)
        # opt['model_file'] = config['world_opt']['model_file']
        # opt['task'] = None
        opt['parlai_home'] = self.parlai_home
        opt['datapath'] = self.parlai_datapath
        opt['download_path'] = self.parlai_download
        opt['safety'] = 'all'
        opt.update(config['world_opt'])
        opt['config'] = config

        return opt

    def setup_interactive(self):
        """
        Build and parse CLI opts.
        """
        self.SHARED['opt'] = self.opt

        self.SHARED['opt']['task'] = 'parlai.agents.local_human.local_human:LocalHumanAgent'

        # Create model and assign it to the specified task
        #import pdb; pdb.set_trace()
        if 'models' in self.opt:
            model_params = {}
            for model in self.opt['models']:
                model_opt = self.opt['models'][model]
                agent = create_agent(model_opt, requireModelExists=True)
        else:
            agent = create_agent(self.opt, requireModelExists=True)
        human_agent = SafeLocalHumanAgent(self.opt)
        self.SHARED['agent'] = agent
        self.SHARED['world'] = create_task(self.SHARED.get('opt'), [human_agent, self.SHARED['agent']])
        #import pdb; pdb.set_trace()


    def _interactive_running(self, opt, reply_text):
        reply = {'episode_done': False, 'text': reply_text}
        self.SHARED['agent'].observe(reply)
        model_res = self.SHARED['agent'].act()
        return model_res

    def dialogue(self, reply_text):
        model_response = self._interactive_running(
            self.SHARED.get('opt'), reply_text
        )

        return model_response['text']
