#!/usr/bin/env python
from galaxygetopt.ggo import GalaxyGetOpt as GGO
#import sys
import logging
logging.basicConfig(level=logging.INFO)


__doc__ = """
Detect Gram Stain
=================

Given a list of genomes to query for, attempt to detect gram stain information
"""

gram_stain_list = {
    'positive': [
        # http://en.wikipedia.org/wiki/Category:Gram-positive_bacteria
        'Actinobacteria',
        'Actinomyces',
        'Actinomyces georgiae',
        'Actinomyces gerencseriae',
        'Actinomyces israelii',
        'Bacillales',
        'Bacillus',
        'Bacillus mojavensis',
        'Bacillus weihenstephanensis',
        'Clostridium',
        'Clostridium acetobutylicum',
        'Clostridium aerotolerans',
        'Clostridium argentinense',
        'Clostridium autoethanogenum',
        'Clostridium baratii',
        'Clostridium beijerinckii',
        'Clostridium bifermentans',
        'Clostridium botulinum',
        'Clostridium butyricum',
        'Clostridium cadaveris',
        'Clostridium cellobioparum',
        'Clostridium cellulolyticum',
        'Clostridium cellulovorans',
        'Clostridium chauvoei',
        'Clostridium clostridioforme',
        'Clostridium colicanis',
        'Clostridium difficile',
        'Clostridium estertheticum',
        'Clostridium fallax',
        'Clostridium formicaceticum',
        'Clostridium histolyticum',
        'Clostridium innocuum',
        'Clostridium kluyveri',
        'Clostridium ljungdahlii',
        'Clostridium novyi',
        'Clostridium paradoxum',
        'Clostridium paraputrificum',
        'Clostridium perfringens',
        'Clostridium phytofermentans',
        'Clostridium piliforme',
        'Clostridium ragsdalei',
        'Clostridium ramosum',
        'Clostridium saccharobutylicum',
        'Clostridium saccharoperbutylacetonicum',
        'Clostridium scatologenes',
        'Clostridium septicum',
        'Clostridium sordellii',
        'Clostridium sporogenes',
        'Clostridium stercorarium',
        'Clostridium sticklandii',
        'Clostridium straminisolvens',
        'Clostridium tertium',
        'Clostridium tetani',
        'Clostridium thermosaccharolyticum',
        'Clostridium tyrobutyricum',
        'Clostridium uliginosum',
        'Corynebacterium',
        'Corynebacterium amycolatum',
        'Corynebacterium bovis',
        'Corynebacterium diphtheriae',
        'Corynebacterium efficiens',
        'Corynebacterium granulosum',
        'Corynebacterium jeikeium',
        'Corynebacterium macginleyi',
        'Corynebacterium minutissimum',
        'Corynebacterium renale',
        'Desulfitobacterium dehalogenans',
        'Enterococcus',
        'Fervidobacterium changbaicum',
        'Fervidobacterium gondwanense',
        'Fervidobacterium islandicum',
        'Georgenia ruanii',
        'Lactobacillales',
        'Listeria',
        'Listeriaceae',
        'Nocardia',
        'Nocardia asteroides',
        'Nocardia brasiliensis',
        'Nocardia farcinica',
        'Nocardia ignorata',
        'Pasteuria',
        'Propionibacterium acnes',
        'Rhodococcus equi',
        'Sarcina',  # (genus)
        'Solobacterium moorei',
        'Sporosarcina',
        'Sporosarcina aquimarina',
        'Sporulation in Bacillus subtilis',
        'Staphylococcus',
        'Staphylococcus aureus',
        'Staphylococcus capitis',
        'Staphylococcus caprae',
        'Staphylococcus epidermidis',
        'Staphylococcus haemolyticus',
        'Staphylococcus hominis',
        'Staphylococcus lugdunensis',
        'Staphylococcus muscae',
        'Staphylococcus nepalensis',
        'Staphylococcus pettenkoferi',
        'Staphylococcus pseudintermedius',
        'Staphylococcus saprophyticus',
        'Staphylococcus schleiferi',
        'Staphylococcus succinus',
        'Staphylococcus warneri',
        'Staphylococcus xylosus',
        'Strangles',
        'Streptococcus',
        'Streptococcus agalactiae',
        'Streptococcus anginosus',
        'Streptococcus bovis',
        'Streptococcus canis',
        'Streptococcus downei',
        'Streptococcus gordonii',
        'Streptococcus iniae',
        'Streptococcus lactarius',
        'Streptococcus mitis',
        'Streptococcus mutans',
        'Streptococcus oralis',
        'Streptococcus parasanguinis',
        'Streptococcus peroris',
        'Streptococcus pneumoniae',
        'Streptococcus pyogenes',
        'Streptococcus ratti',
        'Streptococcus salivarius',
        'Streptococcus sanguinis',
        'Streptococcus sobrinus',
        'Streptococcus suis',
        'Streptococcus thermophilus',
        'Streptococcus tigurinus',
        'Streptococcus uberis',
        'Streptococcus vestibularis',
        'Syntrophomonas curvata',
        'Syntrophomonas palmitatica',
        'Syntrophomonas sapovorans',
        'Syntrophomonas wolfei',
        'Syntrophomonas zehnderi',
        'Viridans streptococci',

        # http://www.nmpdr.org/FIG/wiki/view.cgi/FIG/GramStain
        'Aster yellows witches-broom phytoplasma AYWB',
        'Bacillus anthracis str. \'Ames Ancestor\'',
        'Bacillus anthracis str. A1055',
        'Bacillus anthracis str. Ames',
        'Bacillus anthracis str. Australia 94',
        'Bacillus anthracis str. CNEVA-9066',
        'Bacillus anthracis str. Kruger B',
        'Bacillus anthracis str. Sterne',
        'Bacillus anthracis str. Vollum',
        'Bacillus cereus ATCC 10987',
        'Bacillus cereus ATCC 14579',
        'Bacillus cereus G9241',
        'Bacillus cereus ZK',
        'Bacillus clausii KSM-K16',
        'Bacillus halodurans C-125',
        'Bacillus licheniformis ATCC 14580',
        'Bacillus subtilis subsp. subtilis str. 168',
        'Bacillus thuringiensis serovar konkukian str. 97-27',
        'Bacillus thuringiensis str. Al Hakam',
        'Bacteroides vulgatus ATCC 8482',
        'Bifidobacterium longum',
        'Bifidobacterium longum NCC2705',
        'Brevibacterium linens BL2',
        'Carboxydothermus hydrogenoformans Z-2901',
        'Clostridium acetobutylicum ATCC 824',
        'Clostridium botulinum A str. ATCC 19397',
        'Clostridium botulinum A str. ATCC 3502',
        'Clostridium botulinum A str. Hall',
        'Clostridium difficile 630',
        'Clostridium kluyveri DSM 555',
        'Clostridium perfringens str. 13',
        'Clostridium tetani E88',
        'Clostridium thermocellum ATCC 27405',
        'Corynebacterium diphtheriae NCTC 13129',
        'Corynebacterium efficiens YS-314',
        'Corynebacterium glutamicum ATCC 13032',
        'Corynebacterium jeikeium K411',
        'Dehalococcoides ethenogenes 195',
        'Dehalococcoides sp. CBDB1',
        'Deinococcus radiodurans R1',
        'Enterococcus faecalis V583',
        'Exiguobacterium sp. 255-15',
        'Geobacillus kaustophilus HTA426',
        'Geobacillus thermodenitrificans NG80-2',
        'Janibacter sp. HTCC2649',
        'Lactobacillus acidophilus NCFM',
        'Lactobacillus gasseri',
        'Lactobacillus johnsonii NCC 533',
        'Lactobacillus plantarum WCFS1',
        'Lactococcus lactis subsp. lactis Il1403',
        'Leuconostoc mesenteroides subsp. mesenteroides ATCC 8293',
        'Listeria innocua Clip11262',
        'Listeria monocytogenes 10403S',
        'Listeria monocytogenes Aureli 1997',
        'Listeria monocytogenes EGD-e',
        'Listeria monocytogenes F6900',
        'Listeria monocytogenes FSL J1-194',
        'Listeria monocytogenes FSL J2-071',
        'Listeria monocytogenes J0161',
        'Listeria monocytogenes J2818',
        'Listeria monocytogenes str. 1/2a F6854',
        'Listeria monocytogenes str. 4b F2365',
        'Listeria monocytogenes str. 4b H7858',
        'Listeria welshimeri serovar 6b str. SLCC5334',
        'Methanopyrus kandleri AV19',
        'Methanosphaera stadtmanae DSM 3091',
        'Methanothermobacter thermautotrophicus str. Delta H',
        'Moorella thermoacetica ATCC 39073',
        'Mycobacterium avium subsp. paratuberculosis str. k10',
        'Mycobacterium bovis AF2122/97',
        'Mycobacterium bovis BCG str. Pasteur 1173P2',
        'Mycobacterium leprae TN',
        'Mycobacterium marinum M',
        'Mycobacterium microti OV254',
        'Mycobacterium smegmatis str. MC2 155',
        'Mycobacterium sp. MCS',
        'Mycobacterium tuberculosis',
        'Mycobacterium tuberculosis CDC1551',
        'Mycobacterium tuberculosis F11',
        'Staphylococcus aureus RF122',
        'Staphylococcus aureus subsp. aureus COL',
        'Staphylococcus aureus subsp. aureus JH1',
        'Staphylococcus aureus subsp. aureus JH9',
        'Staphylococcus aureus subsp. aureus MRSA252',
        'Staphylococcus aureus subsp. aureus MSSA476',
        'Staphylococcus aureus subsp. aureus MW2',
        'Staphylococcus aureus subsp. aureus Mu3',
        'Staphylococcus aureus subsp. aureus Mu50',
        'Staphylococcus aureus subsp. aureus N315',
        'Staphylococcus aureus subsp. aureus NCTC 8325',
        'Staphylococcus aureus subsp. aureus USA300',
        'Staphylococcus aureus subsp. aureus str. Newman',
        'Staphylococcus epidermidis',
        'Staphylococcus epidermidis ATCC 12228',
        'Staphylococcus haemolyticus JCSC1435',
        'Staphylococcus saprophyticus subsp. saprophyticus ATCC 15305',
        'Streptococcus agalactiae 2603V/R',
        'Streptococcus agalactiae A909',
        'Streptococcus agalactiae NEM316',
        'Streptococcus gordonii str. Challis substr. CH1',
        'Streptococcus mitis NCTC 12261',
        'Streptococcus mutans UA159',
        'Streptococcus pneumoniae 23F',
        'Streptococcus pneumoniae R6',
        'Streptococcus pneumoniae TIGR4',
        'Streptococcus pyogenes M1 GAS',
        'Streptococcus pyogenes M5',
        'Streptococcus pyogenes MGAS10270',
        'Streptococcus pyogenes MGAS10394',
        'Streptococcus pyogenes MGAS10750',
        'Streptococcus pyogenes MGAS2096',
        'Streptococcus pyogenes MGAS315',
        'Streptococcus pyogenes MGAS5005',
        'Streptococcus pyogenes MGAS6180',
        'Streptococcus pyogenes MGAS8232',
        'Streptococcus pyogenes MGAS9429',
        'Streptococcus pyogenes SSI-1',
        'Streptococcus sanguinis SK36',
        'Streptococcus thermophilus CNRZ1066',
        'Streptococcus thermophilus LMG 18311',
        'Streptococcus uberis 0140J',
        'Ureaplasma parvum serovar 1',
        'Ureaplasma parvum serovar 14',
        'Ureaplasma parvum serovar 3 ATCC 700970',
        'Ureaplasma parvum serovar 6',
        'Ureaplasma urealyticum serovar 10',
        'Ureaplasma urealyticum serovar 11',
        'Ureaplasma urealyticum serovar 12',
        'Ureaplasma urealyticum serovar 13',
        'Ureaplasma urealyticum serovar 4',
        'Ureaplasma urealyticum serovar 5',
        'Ureaplasma urealyticum serovar 7',
        'Ureaplasma urealyticum serovar 8',
        'Ureaplasma urealyticum serovar 9',
    ],
    'negative': [
        # http://en.wikipedia.org/wiki/Category:Gram-negative_bacteria
        'Acetic acid bacteria',
        'Acinetobacter baumannii',
        'Agrobacterium tumefaciens',
        'Anaerobiospirillum',
        'Anaerolinea thermolimosa',
        'Anaerolinea thermophila',
        'Arcobacter',
        'Arcobacter skirrowii',
        'Armatimonas rosea',
        'Bacteroides',
        'Bacteroides fragilis',
        'Bacteroides ruber',
        'Bartonella japonica',
        'Bartonella koehlerae',
        'Bartonella taylorii',
        'Bdellovibrio',
        'Brachyspira',
        'Caldilinea aerophila',
        'Cardiobacterium hominis',
        'Chaperone-Usher fimbriae',
        'Chthonomonas calidirosea',
        'Coxiella burnetii',
        'Cyanobacteria',
        'Cytophaga',
        'Dialister',
        'Enterobacter',
        'Enterobacter cloacae',
        'Enterobacter cowanii',
        'Enterobacteriaceae',
        'Enterobacteriales',
        'Escherichia',
        'Escherichia coli',  # (molecular biology)',
        'Escherichia fergusonii',
        'Fimbriimonas ginsengisoli',
        'Fusobacterium necrophorum',
        'Fusobacterium nucleatum',
        'Fusobacterium polymorphum',
        'Haemophilus felis',
        'Haemophilus haemolyticus',
        'Haemophilus influenzae',
        'Haemophilus pittmaniae',
        'Helicobacter',
        'Helicobacter pylori',
        'Klebsiella pneumoniae',
        'Kluyvera ascorbata',
        'Kluyvera cryocrescens',
        'Legionella',
        'Legionella pneumophila',
        'Leptotrichia buccalis',
        'Levilinea saccharolytica',
        'Luteimonas aestuarii',
        'Luteimonas aquatica',
        'Luteimonas composti',
        'Luteimonas lutimaris',
        'Luteimonas marina',
        'Luteimonas mephitis',
        'Luteimonas vadosa',
        'Megamonas',
        'Megasphaera',
        'Meiothermus',
        'Methylobacterium fujisawaense',
        'Morax-Axenfeld diplobacilli',
        'Moraxella',
        'Moraxella bovis',
        'Moraxella osloensis',
        'Morganella morganii',
        'Negativicutes',
        'Neisseria cinerea',
        'Neisseria gonorrhoeae',
        'Neisseria meningitidis',
        'Neisseria sicca',
        'Nitrosomonas eutropha',
        'Nitrosomonas halophila',
        'Nitrosomonas oligotropha',
        'OMPdb',
        'Pectinatus',
        'Pelosinus',
        'Pontiac fever',
        'Propionispora',
        'Proteobacteria',
        'Proteus mirabilis',
        'Proteus penneri',
        'Pseudomonas',
        'Pseudomonas aeruginosa',
        'Pseudomonas genome database',
        'Pseudomonas luteola',
        'Pseudoxanthomonas broegbernensis',
        'Pseudoxanthomonas japonensis',
        'Rickettsia rickettsii',
        'Salmonella',
        'Salmonella bongori',
        'Salmonella enterica',
        'Salmonella enterica subsp. enterica',
        'Samsonia',
        'Selenomonadales',
        'Serratia marcescens',
        'Shigella',
        'Sorangium cellulosum',
        'Sphaerotilus',
        'Spirochaeta',
        'Spirochaetaceae',
        'Sporomusa',
        'Stenotrophomonas',
        'Stenotrophomonas nitritireducens',
        'Thermotoga neapolitana',
        #'Trimeric autotransporter adhesin',
        'Vampirococcus',
        'Verminephrobacter',
        'Vibrio adaptatus',
        'Vibrio azasii',
        'Vibrio campbellii',
        'Vibrio cholerae',
        'Vitreoscilla',
        'Wolbachia',
        #'YadA bacterial adhesin protein domain',
        'Zymophilus',

        # http://www.nmpdr.org/FIG/wiki/view.cgi/FIG/GramStain
        'Campylobacter jejuni RM1221',
        'Campylobacter jejuni subsp. doylei 269.97',
        'Campylobacter jejuni subsp. jejuni 260.94',
        'Campylobacter jejuni subsp. jejuni 81-176',
        'Campylobacter jejuni subsp. jejuni 84-25',
        'Campylobacter jejuni subsp. jejuni CF93-6',
        'Campylobacter jejuni subsp. jejuni HB93-13',
        'Campylobacter jejuni subsp. jejuni NCTC 11168',
        'Campylobacter coli RM2228',
        'Campylobacter fetus subsp. fetus 82-40',
        'Campylobacter hominis ATCC BAA-381',
        'Campylobacter lari RM2100',
        'Campylobacter upsaliensis RM3195',
        'Chlamydia trachomatis A/HAR-13',
        'Chlamydia trachomatis D/UW-3/CX',
        'Chlamydia muridarum Nigg',
        'Chlamydophila pneumoniae AR39',
        'Chlamydophila pneumoniae CWL029',
        'Chlamydophila pneumoniae J138',
        'Chlamydophila pneumoniae TW-183',
        'Chlamydophila abortus S26/3',
        'Chlamydophila caviae GPIC',
        'Chlamydophila felis Fe/C-56',
        'Haemophilus influenzae 86-028NP',
        'Haemophilus influenzae R2846',
        'Haemophilus influenzae R2866',
        'Haemophilus influenzae Rd KW20',
        'Haemophilus ducreyi 35000HP',
        'Haemophilus somnus 129PT',
        'Haemophilus somnus 2336',
        'Listeria monocytogenes FSL N1-017',
        'Listeria monocytogenes FSL N3-165',
        'Listeria monocytogenes FSL R2-503',
        'Mycoplasma genitalium G-37',
        'Mycoplasma capricolum subsp. capricolum ATCC 27343',
        'Mycoplasma gallisepticum R',
        'Mycoplasma hyopneumoniae 232',
        'Mycoplasma hyopneumoniae 7448',
        'Mycoplasma hyopneumoniae J',
        'Mycoplasma mobile 163K',
        'Mycoplasma mycoides subsp. mycoides SC str. PG1',
        'Mycoplasma penetrans HF-2',
        'Mycoplasma pneumoniae M129',
        'Mycoplasma pulmonis UAB CTIP',
        'Mycoplasma synoviae 53',
        'Neisseria gonorrhoeae FA 1090',
        'Neisseria lactamica ST-640',
        'Neisseria meningitidis FAM18',
        'Neisseria meningitidis MC58',
        'Neisseria meningitidis Z2491',
        'Treponema pallidum subsp. pallidum str. Nichols',
        'Treponema denticola ATCC 35405',
        'Vibrio cholerae 1587',
        'Vibrio cholerae 2740-80',
        'Vibrio cholerae AM-19226',
        'Vibrio cholerae MAK 757',
        'Vibrio cholerae MO10',
        'Vibrio cholerae MZO-3',
        'Vibrio cholerae O1 biovar eltor str. N16961',
        'Vibrio cholerae O395',
        'Vibrio alginolyticus 12G01',
        'Vibrio fischeri ES114',
        'Vibrio harveyi ATCC BAA-1116',
        'Vibrio parahaemolyticus RIMD 2210633',
        'Vibrio sp. Ex25',
        'Vibrio sp. MED222',
        'Vibrio splendidus 12B01',
        'Vibrio vulnificus CMCP6',
        'Vibrio vulnificus YJ016',
        'Aeropyrum pernix K1',
        'Halobacterium sp. NRC-1',
        'Methanococcus maripaludis S2',
        'Pyrobaculum aerophilum str. IM2',
        'Acidobacteria bacterium Ellin345',
        'Acidovorax avenae subsp. citrulli AAC00-1',
        'Acinetobacter baumannii ATCC 17978',
        'Acinetobacter sp. ADP1',
        'Actinobacillus pleuropneumoniae L20',
        'Actinobacillus pleuropneumoniae serovar 1 str. 4074',
        'Agrobacterium tumefaciens str. C58',
        'Alcanivorax borkumensis SK2',
        'Alteromonas macleodii \'Deep ecotype\'',
        'Anaeromyxobacter sp. Fw109-5',
        'Anaplasma marginale str. St. Maries',
        'Anaplasma phagocytophilum HZ',
        'Aquifex aeolicus VF5',
        'Aurantimonas sp. SI85-9A1',
        'Azoarcus sp.',
        'Azotobacter vinelandii',
        'Bacteriovorax marinus SJ',
        'Bacteroides fragilis 638R',
        'Bacteroides fragilis ATCC 25285',
        'Bacteroides fragilis YCH46',
        'Bacteroides thetaiotaomicron VPI-5482',
        'Bartonella bacilliformis KC583',
        'Bartonella henselae str. Houston-1',
        'Bartonella quintana str. Toulouse',
        'Bdellovibrio bacteriovorus HD100',
        'Blochmannia floridanus',
        'Blochmannia pennsylvanicus str. BPEN',
        'Bordetella bronchiseptica RB50',
        'Bordetella parapertussis 12822',
        'Bordetella pertussis Tohama I',
        'Borrelia afzelii PKo',
        'Borrelia burgdorferi B31',
        'Borrelia garinii PBi',
        'Bradyrhizobium japonicum USDA 110',
        'Brucella abortus biovar 1 str. 9-941',
        'Brucella melitensis 16M',
        'Brucella suis 1330',
        'Buchnera aphidicola str. APS',
        'Buchnera aphidicola str. Bp',
        'Buchnera aphidicola str. Sg',
        'Burkholderia ambifaria AMMD',
        'Burkholderia cenocepacia AU 1054',
        'Burkholderia cenocepacia HI2424',
        'Burkholderia cenocepacia J2315',
        'Burkholderia cenocepacia PC184',
        'Burkholderia cepacia R1808',
        'Burkholderia cepacia R18194',
        'Burkholderia dolosa AUO158',
        'Burkholderia fungorum',
        'Burkholderia mallei ATCC 23344',
        'Burkholderia mallei FMH',
        'Burkholderia mallei GB8 horse 4',
        'Burkholderia mallei JHU',
        'Burkholderia mallei NCTC 10247',
        'Burkholderia mallei SAVP1',
        'Burkholderia pseudomallei 1655',
        'Burkholderia pseudomallei 1710a',
        'Burkholderia pseudomallei 1710b',
        'Burkholderia pseudomallei 668',
        'Burkholderia pseudomallei K96243',
        'Burkholderia pseudomallei Pasteur',
        'Burkholderia pseudomallei S13',
        'Burkholderia vietnamiensis strain G4',
        'Burkholderia xenovorans LB400',
        'Caulobacter crescentus CB15',
        'Chlorobium chlorochromatii',
        'Chlorobium phaeobacteroides DSM 266',
        'Chlorobium tepidum TLS',
        'Chromobacterium violaceum ATCC 12472',
        'Chromohalobacter salexigens DSM 3043',
        'Colwellia psychrerythraea 34H',
        'Coxiella burnetii RSA 493',
        'Croceibacter atlanticus HTCC2559',
        'Cytophaga hutchinsonii ATCC 33406',
        'Dechloromonas aromatica RCB',
        'Desulfitobacterium sp. Y51',
        'Desulfotalea psychrophila LSv54',
        'Desulfovibrio desulfuricans G20',
        'Desulfovibrio vulgaris subsp. vulgaris DP4',
        'Desulfovibrio vulgaris subsp. vulgaris str. Hildenborough',
        'Ehrlichia canis str. Jake',
        'Ehrlichia chaffeensis str. Arkansas',
        'Ehrlichia ruminantium str. Gardel',
        'Ehrlichia ruminantium str. Welgevonden',
        'Enterobacter sp. 638',
        'Erwinia carotovora subsp. atroseptica SCRI1043',
        'Erythrobacter litoralis HTCC2594',
        'Erythrobacter sp. NAP1',
        'Escherichia coli 042',
        'Escherichia coli 53638',
        'Escherichia coli APEC O1',
        'Escherichia coli B171',
        'Escherichia coli',
        'Escherichia coli CFT073',
        'Escherichia coli E110019',
        'Escherichia coli E22',
        'Escherichia coli E2348/69',
        'Escherichia coli',
        'Escherichia coli F11',
        'Escherichia coli HS',
        'Escherichia coli K12',
        'Escherichia coli O157:H7',
        'Escherichia coli O157:H7 EDL933',
        'Escherichia coli W3110',
        'Flavobacteria sp. BBFL7',
        'Flavobacteriales bacterium HTCC2170',
        'Flavobacterium psychrophilum JIP02/86',
        'Francisella tularensis subsp. holarctica FTA',
        'Francisella tularensis subsp. holarctica OSU18',
        'Francisella tularensis subsp. novicida U112',
        'Francisella tularensis subsp. tularensis FSC198',
        'Francisella tularensis subsp. tularensis Schu 4',
        'Francisella tularensis subsp. tularensis WY96-3418',
        'Fusobacterium nucleatum subsp. nucleatum ATCC 25586',
        'Geobacter metallireducens GS-15',
        'Geobacter sulfurreducens PCA',
        'Geobacter uraniumreducens Rf4',
        'Gloeobacter violaceus PCC 7421',
        'Gluconobacter oxydans 621H',
        'Gramella forsetii KT0803',
        'Granulibacter bethesdensis CGDNIH1',
        'Hahella chejuensis KCTC 2396',
        'Helicobacter acinonychis str. Sheeba',
        'Helicobacter hepaticus ATCC 51449',
        'Helicobacter mustelae 43772',
        'Helicobacter pylori 26695',
        'Helicobacter pylori J99',
        'Hyphomonas neptunium ATCC 15444',
        'Idiomarina baltica OS145',
        'Idiomarina loihiensis',
        'Legionella pneumophila str. Lens',
        'Legionella pneumophila str. Paris',
        'Legionella pneumophila subsp. pneumophila str. Philadelphia 1',
        'Leifsonia xyli subsp. xyli str. CTCB07',
        'Leptospira interrogans serovar Copenhageni str. Fiocruz L1-130',
        'Leptospira interrogans serovar Lai str. 56601',
        'Loktanella vestfoldensis SKA53',
        'Magnetospirillum gryphiswaldense MSR-1',
        'Magnetospirillum magneticum AMB-1',
        'Mannheimia succiniciproducens',
        'Maricaulis maris MCS10',
        'Mesoplasma florum L1',
        'Mesorhizobium loti MAFF303099',
        'Mesorhizobium sp. BNC1',
        'Methylobacillus flagellatus KT',
        'Methylococcus capsulatus str. Bath',
        'Neorickettsia sennetsu str. Miyayama',
        'Nitrobacter hamburgensis X14',
        'Nitrobacter sp. Nb-311A',
        'Nitrobacter winogradskyi Nb-255',
        'Nitrosococcus oceani ATCC 19707',
        'Nitrosomonas europaea ATCC 19718',
        'Oceanicaulis alexandrii HTCC2633',
        'Oceanicola batsensis HTCC2597',
        'Parachlamydia sp. UWE25',
        'Parvularcula bermudensis HTCC2503',
        'Pasteurella multocida subsp. multocida str. Pm70',
        'Pelagibacter ubique HTCC1062',
        'Pelobacter carbinolicus DSM 2380',
        'Pelodictyon luteolum DSM 273',
        'Petrotoga mobilis SJ95',
        'Photobacterium profundum 3TCK',
        'Photobacterium profundum SS9',
        'Photorhabdus luminescens subsp. laumondii TTO1',
        'Pirellula sp. 1',
        'Polaribacter irgensii 23-P',
        'Polaromonas sp. JS666',
        'Porphyromonas gingivalis W83',
        'Prochlorococcus marinus str. MIT 9211',
        'Prochlorococcus marinus str. MIT 9312',
        'Prochlorococcus marinus str. MIT 9313',
        'Prochlorococcus marinus str.',
        'Prochlorococcus marinus subsp. marinus str. CCMP1375',
        'Prochlorococcus marinus subsp. pastoris str. CCMP1986',
        'Proteus mirabilis HI4320',
        'Pseudoalteromonas atlantica T6c',
        'Pseudoalteromonas haloplanktis TAC125',
        'Pseudoalteromonas tunicata D2',
        'Pseudomonas aeruginosa 2192',
        'Pseudomonas aeruginosa PAO1',
        'Pseudomonas aeruginosa UCBPP-PA14',
        'Pseudomonas entomophila L48',
        'Pseudomonas fluorescens Pf-5',
        'Pseudomonas fluorescens',
        'Pseudomonas fluorescens SBW25',
        'Pseudomonas putida KT2440',
        'Pseudomonas syringae pv. phaseolicola 1448A',
        'Pseudomonas syringae pv. syringae B728a',
        'Pseudomonas syringae pv. tomato str. DC3000',
        'Psychrobacter cryohalolentis K5',
        'Psychrobacter sp. 273-4',
        'Psychromonas sp. CNPT3',
        'Ralstonia eutropha JMP134',
        'Ralstonia solanacearum GMI1000',
        'Rhizobium leguminosarum bv. viciae 3841',
        'Rhodobacter sphaeroides 2.4.1',
        'Rhodobacterales bacterium HTCC2654',
        'Rhodoferax ferrireducens DSM 15236',
        'Rhodopseudomonas palustris',
        'Rhodopseudomonas palustris CGA009',
        'Rickettsia akari str. Hartford',
        'Rickettsia bellii RML369-C',
        'Rickettsia conorii str. Malish 7',
        'Rickettsia felis URRWXCal2',
        'Rickettsia prowazekii str. Madrid E',
        'Rickettsia rickettsii',
        'Rickettsia sibirica',
        'Rickettsia typhi str. Wilmington',
        'Robiginitalea biformata HTCC2501',
        'Roseobacter denitrificans OCh 114',
        'Roseobacter sp. MED193',
        'Roseovarius nubinhibens ISM',
        'Roseovarius sp. 217',
        'Salinibacter ruber DSM 13855',
        'Salmonella enterica subsp. enterica serovar Choleraesuis str. SC-B67',
        'Salmonella enterica subsp. enterica serovar Gallinarum',
        'Salmonella enterica subsp. enterica serovar Paratypi A str. ATCC 9150',
        'Salmonella enterica subsp. enterica serovar Typhi Ty2',
        'Salmonella enterica subsp. enterica serovar Typhi str. CT18',
        'Salmonella typhimurium LT2',
        'Shewanella amazonensis',
        'Shewanella baltica OS155',
        'Shewanella denitrificans OS217',
        'Shewanella frigidimarina NCIMB 400',
        'Shewanella oneidensis MR-1',
        'Shewanella pealeana ATCC 700345',
        'Shewanella putrefaciens CN-32',
        'Shewanella sediminis HAW-EB3',
        'Shewanella sp. MR-4',
        'Shewanella sp. MR-7',
        'Shewanella sp. PV-4',
        'Shewanella sp. W3-18-1',
        'Shewanella sp.ANA-3',
        'Shigella boydii BS512',
        'Shigella dysenteriae M131649',
        'Shigella flexneri 2a str. 2457T',
        'Shigella flexneri 2a str. 301',
        'Shigella sonnei 53G',
        'Shigella sonnei Ss046',
        'Silicibacter pomeroyi DSS-3',
        'Silicibacter sp. TM1040',
        'Sinorhizobium meliloti 1021',
        'Sodalis glossinidius str. \'morsitans\'',
        'Solibacter usitatus Ellin6076',
        'Sorangium cellulosum So ce 56',
        'Sphingomonas wittichii RW1',
        'Sphingopyxis alaskensis RB2256',
        'Stenotrophomonas maltophilia K279a',
        'Sulfitobacter sp. EE-36',
        'Sulfitobacter sp. NAS-14.1',
        'Sulfurovum sp. NBC37-1',
        'Synechococcus elongatus PCC 6301',
        'Synechococcus elongatus PCC 7942',
        'Synechococcus sp. CC9605',
        'Synechococcus sp. CC9902',
        'Synechococcus sp. RS9917',
        'Synechococcus sp. WH 5701',
        'Synechococcus sp. WH 7805',
        'Synechococcus sp. WH 8102',
        'Synechocystis sp. PCC 6803',
        'Syntrophobacter fumaroxidans MPOB',
        'Syntrophus aciditrophicus SB',
        'Tenacibaculum sp. MED152',
        'Thermoanaerobacter tengcongensis MB4',
        'Thermosipho melanesiensis BI429',
        'Thermotoga maritima MSB8',
        'Thermotoga petrophila RKU-1',
        'Thermus thermophilus HB27',
        'Thermus thermophilus HB8',
        'Thiobacillus denitrificans ATCC 25259',
        'Thiomicrospira crunogena XCL-2',
        'Thiomicrospira denitrificans ATCC 33889',
        'Verminephrobacter eiseniae EF01-2',
        'Wigglesworthia glossinidia endosymbiont of Glossina brevipalpis',
        'Wolbachia endosymbiont strain TRS of Brugia malayi',
        'Wolbachia pipientis quinquefasciatus',
        'Wolbachia sp. endosymbiont of Drosophila melanogaster',
        'Wolinella succinogenes DSM 1740',
        'Xanthomonas axonopodis pv. citri str. 306',
        'Xanthomonas campestris pv. campestris ATCC 33913',
        'Xanthomonas campestris pv. campestris str. 8004',
        'Xanthomonas campestris pv. vesicatoria str. 85-10',
        'Xanthomonas oryzae pv. oryzae KACC10331',
        'Xylella fastidiosa 9a5c',
        'Xylella fastidiosa Ann-1',
        'Xylella fastidiosa Temecula1',
        'Yersinia bercovieri ATCC 43970',
        'Yersinia enterocolitica 8081',
        'Yersinia frederiksenii ATCC 33641',
        'Yersinia intermedia ATCC 29909',
        'Yersinia mollaretii ATCC 43969',
        'Yersinia pestis Angola',
        'Yersinia pestis CO92',
        'Yersinia pestis KIM',
        'Yersinia pestis Pestoides F',
        'Yersinia pestis biovar Medievalis str. 91001',
        'Yersinia pseudotuberculosis IP 31758',
        'Yersinia pseudotuberculosis IP 32953',
        'Zymomonas mobilis subsp. mobilis ZM4',
    ]
}


def expand_search_list():
    # First lower case everything.
    gram_stain_list['negative'] = map(lambda x: x.lower(),
                                      gram_stain_list['negative'])
    gram_stain_list['positive'] = map(lambda x: x.lower(),
                                      gram_stain_list['positive'])

    # Then do list expansions
    negative_expand = []
    for strain in gram_stain_list['negative']:
        parts = strain.split(' ')
        for i in range(len(parts) - 1):
            negative_expand.append(' '.join(parts[i:]))
    for i in negative_expand:
        if i not in gram_stain_list['negative']:
            gram_stain_list['negative'].append(i)

    positive_expand = []
    for strain in gram_stain_list['positive']:
        parts = strain.split(' ')
        for i in range(len(parts) - 1):
            positive_expand.append(' '.join(parts[i:]))
    for i in positive_expand:
        if i not in gram_stain_list['positive']:
            gram_stain_list['positive'].append(i)


def find_conflicts():
    for word in gram_stain_list['negative']:
        if word in gram_stain_list['positive']:
            print "Found conflicting name: %s" % word


def annotate_names(data_list=None):
    annotated_data = {
        'Sheet1': {
            'header': ['Bacteria', 'Gram stain of match'],
            'data': []
        }
    }
    for line in data_list.readlines():
        line = line.lower().strip()
        if line in gram_stain_list['negative']:
            annotated_data['Sheet1']['data'].append([
                line, 'negative'
            ])
        elif line in gram_stain_list['positive']:
            annotated_data['Sheet1']['data'].append([
                line, 'positive'
            ])
        else:
            # Couldn't find an extact match, let's find a partial.
            # Since we don't even have a single duplicate match for 1 word
            # phrases (i.e. most significant identifier for bact name),
            # let's just (ab)use startswith
            if ' ' in line:
                if line.split(' ')[0] in \
                        gram_stain_list['negative']:
                    annotated_data['Sheet1']['data'].append([
                        line, 'negative'
                    ])
                elif line.split(' ')[0] in \
                        gram_stain_list['positive']:
                    annotated_data['Sheet1']['data'].append([
                        line, 'positive'
                    ])
                else:
                    annotated_data['Sheet1']['data'].append([
                        line, 'not found'
                    ])
            else:
                # If there isn't a space, it should've matched in the first
                # if/elif. If it missed that it will for sure miss the
                # above if
                annotated_data['Sheet1']['data'].append([
                    line, 'not found'
                ])
    return annotated_data


if __name__ == '__main__':
    # Grab all of the filters from our plugin loader
    opts = GGO(
        options=[
            ['file', 'Single column list of bacterial strains', {'required': True, 'validate':
                                                'File/Input'}],
        ],
        outputs=[
            [
                'results',
                'Input list with gram stain annotated',
                {
                    'validate': 'File/Output',
                    'required': True,
                    'default': 'export',
                    'data_format': 'text/tabular',
                    'default_format': 'TSV_U',
                }
            ]
        ],
        defaults={
            'appid': 'edu.tamu.cpt.generic.GramAnnotator',
            'appname': 'Annotate Gram Stain for Bacteria list',
            'appvers': '1.94',
            'appdesc': 'compares bacteria strain name against a database and attempts to guess gram stain',
        },
        tests=[],
        doc=__doc__
    )
    options = opts.params()
    # Given our initial bacterial name dataset, expand it to include other shortenings of the name.
    expand_search_list()
    # Resolve any conflicting names, don't want to find something as "both negative and positive".
    find_conflicts()
    results = annotate_names(data_list=options['file'])

    from galaxygetopt.outputfiles import OutputFiles
    of = OutputFiles(name='results', GGO=opts)
    of.CRR(data=results)