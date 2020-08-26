#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random

def generator(observed_relevance, categories, no_categories, category_per_item, categories_per_user, no_negatives=10, gen_mode='point'):
    user_input, user_attr, item_i_input, item_i_attr, item_j_input, item_j_attr, labels = [], [], [], [], [], [], []
    no_users, no_items = observed_relevance.shape[0], observed_relevance.shape[1]

    users, items = np.nonzero(observed_relevance)
    positive_set_list = [set() for _ in range(no_users)]
    for (user_id, item_id) in zip(users, items):
        positive_set_list[int(user_id)].add(int(item_id))

    negative_set_list = [set() for _ in range(no_users)]
    for user_id in range(no_users):
        negative_set_list[user_id] = list(set(range(no_items)) - set(positive_set_list[int(user_id)]))

    for index, (user_id, item_id) in enumerate(zip(users, items)):
        if (index % 10000) == 0:
            print('\rComputing instances for interaction', index, '/', len(users), 'of type', gen_mode, end='')

        if gen_mode == 'point':
            user_input.append(user_id)
            item_i_input.append(item_id)
            labels.append(1)

            for _ in range(no_negatives):
                user_input.append(user_id)
                item_i_input.append(random.choice(negative_set_list[user_id]))
                labels.append(0)

        elif gen_mode == 'pair':
            for _ in range(no_negatives):
                user_input.append(user_id)
                item_i_input.append(item_id)
                item_j_input.append(random.choice(negative_set_list[user_id]))
                labels.append(1)

        else:
            raise NotImplementedError('The generation type ' + gen_mode + ' is not implemented.')
    print()

    return (np.array(user_input), np.array(item_i_input),np.array(item_j_input)), (np.array(labels))