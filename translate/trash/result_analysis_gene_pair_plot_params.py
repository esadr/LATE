file_h = 'saver.hd5'
file_h_ori = 'gene_row'  # gene_row/cell_row

tag = '(test_tag)'

data_transformation = 'as_is'  # as_is/log/rpm_log/exp_rpm_log (done on H)

# Gene list
pair_list = [
    # # MBM: Cd34, Gypa, Klf1, Sfpi1
    # ['Cd34', 'Gypa'],
    # ['Klf1', 'Sfpi1'],
    # ['0610007C21Rik;Apr3', 'Hsd17b12'],
    # ['0610007C21Rik;Apr3', 'Magt1'],

    # TEST
    [2, 3],

    # # PBMC G5561 Non-Linear
    # ['ENSG00000173372',
    # 'ENSG00000087086'],
    #
    # ['ENSG00000231389',
    # 'ENSG00000090382'],
    #
    # ['ENSG00000158869',
    # 'ENSG00000090382'],
    #
    # ['ENSG00000074800',
    # 'ENSG00000019582'],
    #
    # ['ENSG00000157873',
    # 'ENSG00000169583'],
    #
    # ['ENSG00000065978',
    # 'ENSG00000139193'],
    #
    # ['ENSG00000117450',
    # 'ENSG00000133112'],
    #
    # ['ENSG00000155366',
    # 'ENSG00000167996'],


]

gene_list = [x for pair in pair_list for x in pair]