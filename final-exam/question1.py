data={
    'a':[{
        'aa':{'aax':5,'aay':6,'aaz':7},
        'ab':{'abx':8,'aby':9,'abz':10}
        },
        {
        'aaa':{'aaax':11,'aaay':12,'aaaz':13},
        'aab':{'aabx':14,'aaby':15,'aabz':16}
        }],
    'b':[{
        'ba':{'bax':17,'bay':18,'baz':19},
        'bb':{'bbx':20,'bby':21,'bbz':22}
        },
        {
        'bba':{'bbax':23,'bbay':24,'bbaz':25},
        'bbb':{'bbbx':26,'bbby':27,'bbbz':28}
        }],
    'c':[{
        'ca':{'cax':29,'cay':30,'caz':31},
        'cb':{'cbx':32,'cby':33,'cbz':34}
        },
        {
        'cca':{'ccax':35,'ccay':36,'ccaz':37},
        'ccb':{'ccbx':38,'ccby':39,'ccbz':40}
        }]
}

for outer_key,outer_val in data.items():
    # print(outer_key,outer_val)
    for list_item in outer_val:
        # print(list_item)
        for outer_inner_key,outer_inner_val in list_item.items():
            # print(outer_inner_key,outer_inner_val)
            for inner_key,inner_value in outer_inner_val.items():
                print(f'Key:{inner_key} value:{inner_value}')
