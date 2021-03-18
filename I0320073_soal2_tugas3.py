print("SOAL 2")

dict = {'Nama': 'Narista Neri Vadila',
        'Hobi': 'Bernyanyi, menonton film, dan membaca wattpad',
        'Sosial media': 'Intagram:@naristanv, line:@naristanv, dan WA:081548650853',
        'Lagu kesukaan': 'Stay With Me - Chanyeol ft Punch, Yours - Raiden X Chanyeol ft LeeHi Changmo dan Sampai Jadi Debu - Banda Neira',
        'Makanan favorit': 'Indomie, bakso, dan ayam goreng'}
print("dict['Nama']: ", dict['Nama'])
print("dict['Hobi']: ", dict['Hobi'])
print("dict['Sosial media']: ", dict['Sosial media'])
print("dict['Lagu kesukaan']: ", dict['Lagu kesukaan'])
print("dict['Makanan favorit']: ", dict['Makanan favorit'])
print("Dict: ", dict)

print("Mengganti salah satu nilai dalam dictionary: ")

dict = {'Nama': 'Narista Neri Vadila',
        'Hobi': 'Bernyanyi, menonton film, dan membaca wattpad',
        'Sosial media': 'Instagram:@naristanv, line:@naristanv, dan WA:081548650853',
        'Lagu kesukaan': 'Stay With Me - Chanyeol ft Punch, Yours - Raiden X Chanyeol ft LeeHi Changmo dan Sampai Jadi Debu - Banda Neira',
        'Makanan favorit': 'Indomie, bakso, dan ayam goreng'}
dict['Hobi'] = 'Bernyanyi, menonton film dan berlibur'
dict['Sosial media'] = 'Instagram:@naristanv, line:@naristanv dan twitter:@naristanv'
print("dict['Hobi']: ", dict['Hobi'])
print("dict['Sosial media']: ", dict['Sosial media'])
del dict['Makanan favorit']
print("Dict: ", dict)

#Menambah item pada dictionary
print("Menambah item pada dictionary: ")
dict = {'Nama': 'Narista Neri Vadila',
        'Hobi': 'Bernyanyi, menonton film, dan membaca wattpad',
        'Sosial media': 'Intagram:@naristanv, line:@naristanv, dan WA:081548650853',
        'Lagu kesukaan': 'Stay With Me - Chanyeol ft Punch, Yours - Raiden X Chanyeol ft LeeHi Changmo dan Sampai Jadi Debu - Banda Neira',
        'Makanan favorit': 'Indomie, bakso, dan ayam goreng'}
dict.update({'Hobi': 'Bernyanyi, menonton film, membaca wattpad, dan mendengarkan musik'})
print("Dict: ", dict)

