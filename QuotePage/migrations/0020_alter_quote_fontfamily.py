# Generated by Django 5.1 on 2024-08-31 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuotePage', '0019_alter_quote_fontfamily'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='fontfamily',
            field=models.CharField(choices=[('arial', 'arial'), ('arialbd', 'arialbd'), ('arialbi', 'arialbi'), ('ariali', 'ariali'), ('ariblk', 'ariblk'), ('bahnschrift', 'bahnschrift'), ('calibri', 'calibri'), ('calibrib', 'calibrib'), ('calibrii', 'calibrii'), ('calibril', 'calibril'), ('calibrili', 'calibrili'), ('calibriz', 'calibriz'), ('cambriab', 'cambriab'), ('cambriai', 'cambriai'), ('cambriaz', 'cambriaz'), ('Candara', 'Candara'), ('Candarab', 'Candarab'), ('Candarai', 'Candarai'), ('Candaral', 'Candaral'), ('Candarali', 'Candarali'), ('Candaraz', 'Candaraz'), ('comic', 'comic'), ('comicbd', 'comicbd'), ('comici', 'comici'), ('comicz', 'comicz'), ('consola', 'consola'), ('consolab', 'consolab'), ('consolai', 'consolai'), ('consolaz', 'consolaz'), ('constan', 'constan'), ('constanb', 'constanb'), ('constani', 'constani'), ('constanz', 'constanz'), ('corbel', 'corbel'), ('corbelb', 'corbelb'), ('corbeli', 'corbeli'), ('corbell', 'corbell'), ('corbelli', 'corbelli'), ('corbelz', 'corbelz'), ('cour', 'cour'), ('courbd', 'courbd'), ('courbi', 'courbi'), ('couri', 'couri'), ('ebrima', 'ebrima'), ('ebrimabd', 'ebrimabd'), ('framd', 'framd'), ('framdit', 'framdit'), ('Gabriola', 'Gabriola'), ('gadugi', 'gadugi'), ('gadugib', 'gadugib'), ('georgia', 'georgia'), ('georgiab', 'georgiab'), ('georgiai', 'georgiai'), ('georgiaz', 'georgiaz'), ('himalaya', 'himalaya'), ('holomdl2', 'holomdl2'), ('impact', 'impact'), ('Inkfree', 'Inkfree'), ('javatext', 'javatext'), ('LeelaUIb', 'LeelaUIb'), ('LeelawUI', 'LeelawUI'), ('LeelUIsl', 'LeelUIsl'), ('lucon', 'lucon'), ('l_10646', 'l_10646'), ('malgun', 'malgun'), ('malgunbd', 'malgunbd'), ('malgunsl', 'malgunsl'), ('micross', 'micross'), ('mmrtext', 'mmrtext'), ('mmrtextb', 'mmrtextb'), ('monbaiti', 'monbaiti'), ('msyi', 'msyi'), ('mtextra', 'mtextra'), ('mvboli', 'mvboli'), ('Nirmala', 'Nirmala'), ('NirmalaB', 'NirmalaB'), ('NirmalaS', 'NirmalaS'), ('ntailu', 'ntailu'), ('ntailub', 'ntailub'), ('pala', 'pala'), ('palab', 'palab'), ('palabi', 'palabi'), ('palai', 'palai'), ('phagspa', 'phagspa'), ('phagspab', 'phagspab'), ('segmdl2', 'segmdl2'), ('SegoeIcons', 'SegoeIcons'), ('segoepr', 'segoepr'), ('segoeprb', 'segoeprb'), ('segoesc', 'segoesc'), ('segoescb', 'segoescb'), ('segoeui', 'segoeui'), ('segoeuib', 'segoeuib'), ('segoeuii', 'segoeuii'), ('segoeuil', 'segoeuil'), ('segoeuisl', 'segoeuisl'), ('segoeuiz', 'segoeuiz'), ('seguibl', 'seguibl'), ('seguibli', 'seguibli'), ('seguiemj', 'seguiemj'), ('seguihis', 'seguihis'), ('seguili', 'seguili'), ('seguisb', 'seguisb'), ('seguisbi', 'seguisbi'), ('seguisli', 'seguisli'), ('seguisym', 'seguisym'), ('SegUIVar', 'SegUIVar'), ('simsunb', 'simsunb'), ('SitkaVF-Italic', 'SitkaVF-Italic'), ('SitkaVF', 'SitkaVF'), ('sylfaen', 'sylfaen'), ('symbol', 'symbol'), ('tahoma', 'tahoma'), ('tahomabd', 'tahomabd'), ('taile', 'taile'), ('taileb', 'taileb'), ('times', 'times'), ('timesbd', 'timesbd'), ('timesbi', 'timesbi'), ('timesi', 'timesi'), ('trebuc', 'trebuc'), ('trebucbd', 'trebucbd'), ('trebucbi', 'trebucbi'), ('trebucit', 'trebucit'), ('verdana', 'verdana'), ('verdanab', 'verdanab'), ('verdanai', 'verdanai'), ('verdanaz', 'verdanaz'), ('webdings', 'webdings'), ('wingding', 'wingding')], default='arial', help_text='Choose a Font for Your Quote!', max_length=50),
        ),
    ]
