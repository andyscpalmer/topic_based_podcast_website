# Generated by Django 3.0 on 2020-03-31 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EpisodeTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=300)),
                ('net_worth', models.DecimalField(decimal_places=2, help_text='Number in billions up to two decimal points.', max_digits=6)),
                ('net_worth_source', models.CharField(blank=True, help_text="Short name of source of net worth, e.g. 'Forbes'.", max_length=50, null=True)),
                ('net_worth_source_date', models.CharField(blank=True, help_text="Year or month and year net worth was reported, e.g. '2020' or 'March 2020'.", max_length=50, null=True)),
                ('net_worth_source_link', models.URLField(blank=True, help_text="URL of net worth source, e.g. 'https://www.forbes.com/profile/jeff-bezos/'", null=True)),
                ('topic_bio', models.TextField(help_text='Do not include citations here. Add those after the page is created.HTML is available, but please only use for links and basic styling.')),
                ('topic_pic_filename', models.CharField(default='grubman.png', help_text="Filename of image uploaded to AWS topics folder, e.g. 'epstein.png'.", max_length=200)),
                ('topic_pic_caption', models.CharField(blank=True, help_text='Image attribution and/or caption.', max_length=500, null=True)),
                ('slug', models.SlugField(max_length=300, unique=True)),
            ],
            options={
                'ordering': ['-net_worth'],
            },
        ),
        migrations.CreateModel(
            name='TopicCitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citation_title', models.CharField(help_text='e.g.: Jeffrey Epstein Gave Millions to Charity, Study Finds', max_length=500)),
                ('citation_publication', models.CharField(help_text="Source, e.g. 'New York Times'.", max_length=100)),
                ('citation_link', models.URLField(help_text='Article link.', max_length=500)),
                ('archive_link_available', models.BooleanField(default=False, help_text='Select to display a backup link from the internet archive.')),
                ('archive_link', models.URLField(blank=True, help_text='A link from the web archive to supplement original.', max_length=500, null=True)),
                ('citation_description', models.TextField(help_text='One to two sentence overview of citation contents.')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citations', to='content.Topic')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.RemoveField(
            model_name='billionairecitation',
            name='billionaire',
        ),
        migrations.RemoveField(
            model_name='episodebillionaire',
            name='billionaire',
        ),
        migrations.RemoveField(
            model_name='episodebillionaire',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='show_billionaires',
        ),
        migrations.AddField(
            model_name='episode',
            name='show_topics',
            field=models.BooleanField(default=False, help_text='Select this to display topics linked to this episode.'),
        ),
        migrations.DeleteModel(
            name='Billionaire',
        ),
        migrations.DeleteModel(
            name='BillionaireCitation',
        ),
        migrations.DeleteModel(
            name='EpisodeBillionaire',
        ),
        migrations.AddField(
            model_name='topic',
            name='episode',
            field=models.ManyToManyField(blank=True, related_name='topics', through='content.EpisodeTopic', to='content.Episode'),
        ),
        migrations.AddField(
            model_name='episodetopic',
            name='episode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Episode'),
        ),
        migrations.AddField(
            model_name='episodetopic',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='content.Topic'),
        ),
    ]
