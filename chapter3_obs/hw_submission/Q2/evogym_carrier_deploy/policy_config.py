exp_config = {
    'type': 'ppo',
    'on_policy': True,
    'cuda': True,
    'action_space': 'continuous',
    'discount_factor': 0.99,
    'gae_lambda': 0.95,
    'epoch_per_collect': 10,
    'batch_size': 256,
    'learning_rate': 0.003,
    'weight_decay': 0,
    'value_weight': 0.5,
    'entropy_weight': 0.01,
    'clip_ratio': 0.2,
    'adv_norm': True,
    'value_norm': True,
    'ppo_param_init': True,
    'grad_norm': 0.5,
    'n_sample': 2048,
    'unroll_len': 1,
    'deterministic_eval': True,
    'model': {},
    'cfg_type': 'PPOFPolicyDict'
}
