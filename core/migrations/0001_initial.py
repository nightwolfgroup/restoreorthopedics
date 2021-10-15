# Generated by Django 3.1.2 on 2020-10-15 07:45

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
                ('message', models.TextField(max_length=2000)),
                ('staff_notes', models.TextField(blank=True, help_text='Internal notes for staff communication', null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='email')),
                ('viewed', models.BooleanField(default=False)),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-sent_on'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('quote', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('taggit.tag',),
        ),
        migrations.CreateModel(
            name='TestimonialPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'verbose_name': 'Testimonial Page',
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, default='https://www.facebook.com/RestoreOrthopedics/', help_text='Facebook URL', null=True)),
                ('twitter', models.URLField(blank=True, default='https://twitter.com/OrthoSonora', help_text='Twitter URL', null=True)),
                ('instagram', models.URLField(blank=True, default='https://www.instagram.com/restoreorthobiologic/', help_text='Instagram URL', null=True)),
                ('google', models.URLField(blank=True, default='https://g.page/restoreorthosonora?gm', help_text='Google Business URL', null=True)),
                ('youtube', models.URLField(blank=True, default='https://www.youtube.com/channel/UCzw1usochiCFXobpi5omsoA', help_text='YouTube Channel URL', null=True, verbose_name='YouTube')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Social Media Accounts',
            },
        ),
        migrations.CreateModel(
            name='LegalPost',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('content', wagtail.core.fields.StreamField([('legal_article', wagtail.core.blocks.StructBlock([('page_content', wagtail.core.blocks.RichTextBlock(required=True)), ('related_articles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('related_article_name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('related_article_link', wagtail.core.blocks.PageChooserBlock(required=False))], icon='fa-window-restore'), label='Related Articles'))]))])),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'verbose_name': 'Legal Policy',
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='LegalPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('subtitle', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image displayed behind title text with gradient overlay', label='Background Image', required=False))]))])),
                ('content', wagtail.core.fields.StreamField([('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Optional title to display above cards', max_length=100, required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('fe-activity', 'Activity'), ('fe-airplay', 'AirPlay'), ('fe-alert-circle', 'Alert Circle'), ('fe-alert-octagon', 'Alert Octagon'), ('fe-alert-triangle', 'Alert Triangle'), ('fe-align-center', 'Align Center'), ('fe-align-justify', 'Align Justify'), ('fe-align-left', 'Align Left'), ('fe-align-right', 'Align Right'), ('fe-anchor', 'Anchor'), ('fe-aperture', 'Aperture'), ('fe-archive', 'Archive'), ('fe-arrow-down-circle', 'Arrow Down Circle'), ('fe-arrow-down-left', 'Arrow Down Left'), ('fe-arrow-down-right', 'Arrow Down Right'), ('fe-arrow-down', 'Arrow Down'), ('fe-arrow-left-circle', 'Arrow Left Circle'), ('fe-arrow-left', 'Arrow Left'), ('fe-arrow-right-circle', 'Arrow Right Circle'), ('fe-arrow-right', 'Arrow Right'), ('fe-arrow-up-circle', 'Arrow Up Circle'), ('fe-arrow-up-left', 'Arrow Up Left'), ('fe-arrow-up-right', 'Arrow Up Right'), ('fe-arrow-up', 'Arrow Up'), ('fe-at-sign', 'At Sign'), ('fe-award', 'Award'), ('fe-bar-chart-2', 'Bar Chart 2'), ('fe-bar-chart', 'Bar Chart'), ('fe-battery-charging', 'Battery Charging'), ('fe-battery', 'Battery'), ('fe-behance', 'Behance'), ('fe-bell-off', 'Bell Off'), ('fe-bell', 'Bell'), ('fe-bluetooth', 'Bluetooth'), ('fe-bold', 'Bold'), ('fe-book-open', 'Open Book'), ('fe-book', 'Book'), ('fe-bookmark', 'Bookmark'), ('fe-box', 'Box'), ('fe-briefcase', 'Briefcase'), ('fe-calendar', 'Calendar'), ('fe-camera-off', 'Camera Off'), ('fe-camera', 'Camera'), ('fe-cast', 'Cast'), ('fe-check-circle', 'Check Circle'), ('fe-check-square', 'Check Square'), ('fe-check', 'Check'), ('fe-chevron-down', 'Chevron Down'), ('fe-chevron-left', 'Chevron Left'), ('fe-chevron-right', 'Chevron Right'), ('fe-chevron-up', 'Chevron Up'), ('fe-chevron-down', 'Chevron Down'), ('fe-chevrons-left', 'Chevrons Left'), ('fe-chevrons-right', 'Chevrons Right'), ('fe-chevrons-up', 'Chevrons Up'), ('fe-chrome', 'Chrome'), ('fe-clipboard', 'Clipboard'), ('fe-clock', 'Clock'), ('fe-cloud-drizzle', 'Cloud Drizzle'), ('fe-cloud-lightning', 'Cloud Lightning'), ('fe-cloud-off', 'Cloud Off'), ('fe-cloud-rain', 'Cloud Rain'), ('fe-cloud-snow', 'Cloud Snow'), ('fe-cloud', 'Cloud'), ('fe-code', 'Code'), ('fe-codepen', 'Codepen'), ('fe-codesandbox', 'Code Sandbox'), ('fe-coffee', 'Coffee'), ('fe-columns', 'Columns'), ('fe-command', 'Command'), ('fe-compass', 'Compass'), ('fe-copy', 'Copy'), ('fe-corner-down-left', 'Corner Down Left'), ('fe-corner-down-right', 'Corner Down Right'), ('fe-corner-left-down', 'Corner Left Down'), ('fe-corner-left-up', 'Corner Left Up'), ('fe-corner-right-down', 'Corner Right Down'), ('fe-corner-right-up', 'Corner Right Up'), ('fe-corner-up-left', 'Corner Up Left'), ('fe-corner-up-right', 'Corner Up Right'), ('fe-cpu', 'CPU'), ('fe-credit-card', 'Credit Card'), ('fe-crop', 'Crop'), ('fe-crosshair', 'Crosshair'), ('fe-database', 'Database'), ('fe-delete', 'Delete'), ('fe-disc', 'Disc'), ('fe-dollar-sign', 'Dollar Sign'), ('fe-download-cloud', 'Download Cloud'), ('fe-download', 'Download'), ('fe-dribbble', 'Dribble'), ('fe-droplet', 'Droplet'), ('fe-edit-2', 'Edit 2'), ('fe-edit-3', 'Edit 3'), ('fe-edit', 'Edit'), ('fe-external-link', 'External Link'), ('fe-eye-off', 'Eye Off'), ('fe-eye', 'Eye'), ('fe-facebook', 'Facebook'), ('fe-fast-forward', 'Fast Forward'), ('fe-feather', 'Feather'), ('fe-figma', 'Figma'), ('fe-file-minus', 'File Minus'), ('fe-file-plus', 'File Plus'), ('fe-file-text', 'File Text'), ('fe-file', 'File'), ('fe-film', 'Film'), ('fe-filter-alt', 'Filter Alt'), ('fe-filter', 'Filter'), ('fe-flag', 'Flag'), ('fe-folder-minus', 'Folder Minus'), ('fe-folder-plus', 'Folder Plus'), ('fe-folder', 'Folder'), ('fe-framer', 'Framer'), ('fe-frown', 'Frown'), ('fe-gift', 'Gift'), ('fe-git-branch', 'Git Branch'), ('fe-git-commit', 'Git Commit'), ('fe-git-merge', 'Git Merge'), ('fe-git-pull-request', 'Git Pull Request'), ('fe-github', 'Github'), ('fe-gitlab', 'Gitlab'), ('fe-globe', 'Globe'), ('fe-google', 'Google'), ('fe-grid', 'Grid'), ('fe-hangouts', 'Hangouts'), ('fe-hard-drive', 'Hard Drive'), ('fe-hash', 'Hash'), ('fe-headphones', 'Headphones'), ('fe-heart', 'Heart'), ('fe-help-circle', 'Help Circle'), ('fe-hexagon', 'Hexagon'), ('fe-home', 'Home'), ('fe-image', 'Image'), ('fe-inbox', 'Inbox'), ('fe-info', 'Info'), ('fe-instagram', 'Instagram'), ('fe-italic', 'Italic'), ('fe-key', 'Key'), ('fe-layers', 'Layers'), ('fe-layout', 'Layout'), ('fe-life-buoy', 'Life Bouy'), ('fe-link-2', 'Link 2'), ('fe-link', 'Link'), ('fe-linkedin', 'Linkedin'), ('fe-list', 'List'), ('fe-loader', 'Loader'), ('fe-lock', 'Lock'), ('fe-log-in', 'Log In'), ('fe-log-out', 'Log Out'), ('fe-mail', 'Mail'), ('fe-map-pin', 'Map Pin'), ('fe-map', 'Map'), ('fe-maximize-2', 'Maximize 2'), ('fe-maximize', 'Maximize'), ('fe-meh', 'Meh'), ('fe-menu', 'Menu'), ('fe-message-circle', 'Message Circle'), ('fe-message-square', 'Message Square'), ('fe-messenger', 'Messenger'), ('fe-mic-off', 'Microphone Mute'), ('fe-mic', 'Microphone'), ('fe-minimize-2', 'Minimize 2'), ('fe-minimize', 'Minimize'), ('fe-minus-circle', 'Minus Circle'), ('fe-minus-square', 'Minus Square'), ('fe-minus', 'Minus'), ('fe-monitor', 'Monitor'), ('fe-moon', 'Moon'), ('fe-more-horizontal', 'More Horizontal'), ('fe-more-vertical', 'More Vertical'), ('fe-mouse-pointer', 'Mouse Pointer'), ('fe-move', 'Move'), ('fe-music', 'Music'), ('fe-navigation-2', 'Navigation 2'), ('fe-navigation', 'Navigation'), ('fe-octagon', 'Octagon'), ('fe-package', 'Package'), ('fe-paperclip', 'Paperclip'), ('fe-pause-circle', 'Pause Circle'), ('fe-pause', 'Pause'), ('fe-paypal', 'PayPal'), ('fe-pen-tool', 'Pen Tool'), ('fe-percent', 'Percent'), ('fe-phone-call', 'Phone Call'), ('fe-phone-forwarded', 'Phone Forwarded'), ('fe-phone-incoming', 'Phone Call Incoming'), ('fe-phone-missed', 'Phone Call Missed'), ('fe-phone-off', 'Phone Off'), ('fe-phone-outgoing', 'Phone Outgoing'), ('fe-phone', 'Phone'), ('fe-pie-chart', 'Pie Chart'), ('fe-pinterest', 'Pinterest'), ('fe-play-circle', 'Play Circle'), ('fe-play', 'Play'), ('fe-plus-circle', 'Plus Circle'), ('fe-plus-square', 'Plus Square'), ('fe-plus', 'Plus'), ('fe-pocket', 'Pocket'), ('fe-power', 'Power'), ('fe-printer', 'Printer'), ('fe-quotes', 'Quotes'), ('fe-radio', 'Radio'), ('fe-refresh-ccw', 'Refresh CCW'), ('fe-refresh-cw', 'Refresh CW'), ('fe-repeat', 'Repeat'), ('fe-rewind', 'Rewind'), ('fe-rotate-ccw', 'Rotate CCW'), ('fe-rotate-cw', 'Rotate CW'), ('fe-rss', 'RSS Feed'), ('fe-save', 'Save'), ('fe-scissors', 'Scissors'), ('fe-search', 'Search'), ('fe-send', 'Send'), ('fe-server', 'Server'), ('fe-settings', 'Settings'), ('fe-share-2', 'Share 2'), ('fe-share', 'Share'), ('fe-shield-off', 'Shield-Off'), ('fe-shield', 'Shield'), ('fe-shopping-bag', 'Shopping Bag'), ('fe-shopping-cart', 'Shopping Cart'), ('fe-shuffle', 'Shuffle'), ('fe-sidebar', 'Sidebar'), ('fe-skip-back', 'Skip Back'), ('fe-skip-forward', 'Skip Forward'), ('fe-skype', 'Skype'), ('fe-slack', 'Slack'), ('fe-slash', 'Slash'), ('fe-sliders', 'Sliders'), ('fe-smartphone', 'Smartphone'), ('fe-smile', 'Smile'), ('fe-speaker', 'Speaker'), ('fe-star', 'Star'), ('fe-stop-circle', 'Stop Circle'), ('fe-sun', 'Sun'), ('fe-sunrise', 'Sunrise'), ('fe-sunset', 'Sunset'), ('fe-tablet', 'Tablet'), ('fe-tag', 'Tag'), ('fe-target', 'Target'), ('fe-telegram', 'Telegram'), ('fe-terminal', 'Terminal'), ('fe-thermometer', 'Thermometer'), ('fe-thumbs-down', 'Thumbs Down'), ('fe-thumbs-up', 'Thumbs Up'), ('fe-toggle-left', 'Toggle Left'), ('fe-toggle-right', 'Toggle Right'), ('fe-tool', 'Tool'), ('fe-trash-2', 'Trash 2'), ('fe-trash', 'Trash'), ('fe-trello', 'Trello'), ('fe-trending-down', 'Trending Down'), ('fe-trending-up', 'Trending Up'), ('fe-truck', 'Truck'), ('fe-tumblr', 'Tumblr'), ('fe-tv', 'TV'), ('fe-twitch', 'Twitch'), ('fe-twitter', 'Twitter'), ('fe-type', 'Type'), ('fe-umbrella', 'Umbrella'), ('fe-underline', 'Underline'), ('fe-unlock', 'Unlock'), ('fe-upload-cloud', 'Upload Cloud'), ('fe-upload', 'Upload'), ('fe-user-check', 'User Check'), ('fe-user-minus', 'User Minus'), ('fe-user-plus', 'User Plus'), ('fe-user-x', 'User X'), ('fe-user', 'User'), ('fe-users', 'Users'), ('fe-viber', 'Viber'), ('fe-video-off', 'Video Off'), ('fe-video', 'Video'), ('fe-vimeo', 'Vimeo'), ('fe-vk', 'VK'), ('fe-voicemail', 'Voicemail'), ('fe-volume-1', 'Volume 1'), ('fe-volume-2', 'Volume 2'), ('fe-volume-x', 'Volume X'), ('fe-volume', 'Volume'), ('fe-watch', 'Watch'), ('fe-wechat', 'WeChat'), ('fe-wifi-off', 'WiFi Off'), ('fe-wifi', 'WiFi'), ('fe-wind', 'Wind'), ('fe-x-circle', 'X Circle'), ('fe-x-octagon', 'X Octagon'), ('fe-x-square', 'X Square'), ('fe-x', 'X'), ('fe-youtube', 'YouTube'), ('fe-zap-off', 'Zap Off'), ('fe-zap', 'Zap'), ('fe-zoom-in', 'Zoom In'), ('fe-zoom-out', 'Zoom Out')], help_text='Icon to display at top of card', max_length=20, required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='Card Title', max_length=30, required=True)), ('text', wagtail.core.blocks.CharBlock(help_text='Card Text', max_length=200, required=True)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn more', max_length=50, required=True)), ('button_link', wagtail.core.blocks.PageChooserBlock(required=True))], icon='fa-clone')))])), ('help', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default="Haven't found the answer? We can help.", max_length=100, required=True)), ('button_text', wagtail.core.blocks.CharBlock(default='Send us a Message', max_length=50, required=True)), ('button_link', wagtail.core.blocks.PageChooserBlock(required=True)), ('subtext', wagtail.core.blocks.CharBlock(default='Contact us and we’ll get back to you as soon as possible.', max_length=200, required=True)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('secondary', 'Light Gray'), ('light', 'White')]))]))])),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'verbose_name': 'Legal Home Page',
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Restore Your Healthy & Active Lifestyle!', help_text='Homepage title text', required=True)), ('buttons', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(help_text='Text displayed within the button', required=False)), ('button_link', wagtail.core.blocks.PageChooserBlock(help_text='Link to page which the button will go to when clicked', required=False))], icon='fa-hand-o-up'))), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Main image displayed on the homepage', required=True)), ('icon_one', wagtail.images.blocks.ImageChooserBlock(help_text='Icon to display next to Doctor name', required=False)), ('icon_two', wagtail.images.blocks.ImageChooserBlock(help_text='Icon to display next to Doctor name', required=False))]))])),
                ('content', wagtail.core.fields.StreamField([('services', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Our services', help_text='Section title', required=True)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='Text displayed beneath title', required=False)), ('card', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('Icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('Description', wagtail.core.blocks.TextBlock(max_length=255, required=True))], icon='fa-medkit')))])), ('testimonials', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='What People Say About Us', max_length=100, required=False))])), ('CTA', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('subtitle', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=True))], icon='fa-link'))), ('background_image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('map', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Restore Orthopedics & Sports Medicine, Dr. Ariana DeMers, DO', max_length=200, required=True)), ('address', wagtail.core.blocks.CharBlock(default='13949 Mono Way, Sonora, CA 95370', max_length=255, required=True)), ('phone_number', wagtail.core.blocks.CharBlock(default='(209) 533 5371', max_length=255, required=True)), ('email', wagtail.core.blocks.EmailBlock(default='admin@restoreorthobiologic.com', max_length=255, required=True)), ('map_link', wagtail.core.blocks.URLBlock(default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3145.0021611358766!2d-120.34119008383189!3d37.977078879722995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8090c528b63b1ba3%3A0xb75939887ae2279d!2sRestore%20Orthopedics%20and%20Sports%20Medicine%3A%20Ariana%20DeMers%2C%20D.O.!5e0!3m2!1sen!2sus!4v1601053197881!5m2!1sen!2sus', max_length=2000, required=True))])), ('FAQ', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Patient Resources', max_length=100, required=True)), ('card', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('subtitle', wagtail.core.blocks.TextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(max_length=100, required=True))], icon='fa-tag'))), ('faq', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('answer', wagtail.core.blocks.RichTextBlock(required=True)), ('question_number', wagtail.core.blocks.IntegerBlock(required=True))], icon='fa-question'), label='Frequently Asked Questions'))])), ('latest_blog', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Our Blog', max_length=100, required=True))]))])),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'verbose_name': 'Home Page',
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(default='We will get back to you as soon as possible!', max_length=255)),
                ('background_image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='background_image', to='wagtailimages.image', verbose_name='Background Image')),
                ('map_image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contact_map_image', to='wagtailimages.image', verbose_name='Map Image')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'verbose_name': 'Contact Page',
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='BusinessSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Restore Orthopedics & Sports Medicine', max_length=255, null=True, verbose_name='Name')),
                ('street_address', models.CharField(default='13949 Mono Way', max_length=255, null=True, verbose_name='Street')),
                ('city', models.CharField(default='Sonora', max_length=255, verbose_name='City')),
                ('state', models.CharField(default='CA', max_length=2, verbose_name='State')),
                ('zip', models.CharField(default='95370', max_length=5, verbose_name='Zip')),
                ('phone', models.CharField(default='(209) 533-5371', max_length=255, null=True, verbose_name='Phone')),
                ('fax', models.CharField(default='(209) 533-5372', max_length=255, null=True, verbose_name='Fax')),
                ('email', models.EmailField(default='admin@restoreorthobiologic.com', max_length=254, null=True, verbose_name='Email')),
                ('sunday_hours', models.CharField(default='Closed', max_length=20, verbose_name='Sunday')),
                ('monday_hours', models.CharField(default='8:00 AM - 4:30 PM', max_length=20, verbose_name='Monday')),
                ('tuesday_hours', models.CharField(default='8:00 AM - 4:30 PM', max_length=20, verbose_name='Tuesday')),
                ('wednesday_hours', models.CharField(default='8:00 AM - 4:30 PM', max_length=20, verbose_name='Wednesday')),
                ('thursday_hours', models.CharField(default='8:00 AM - 4:30 PM', max_length=20, verbose_name='Thursday')),
                ('friday_hours', models.CharField(default='8:00 AM - 4:30 PM', max_length=20, verbose_name='Friday')),
                ('saturday_hours', models.CharField(default='Closed', max_length=20, verbose_name='Saturday')),
                ('logo_dark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='logo_dark', to='wagtailimages.image', verbose_name='Main (dark)')),
                ('logo_footer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='logo_footer', to='wagtailimages.image', verbose_name='Footer')),
                ('logo_footer_alt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='logo_footer_alt', to='wagtailimages.image', verbose_name='Footer (alt)')),
                ('logo_icon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='logo_icon', to='wagtailimages.image', verbose_name='Icon')),
                ('logo_icon_footer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='logo_icon_footer', to='wagtailimages.image', verbose_name='Footer icon')),
                ('logo_light', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='logo_light', to='wagtailimages.image', verbose_name='Main (light)')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Our Commitment to You', max_length=30, required=True)), ('subtitle', wagtail.core.blocks.CharBlock(default='Our Goals. Our Mission.', max_length=50, required=True)), ('blockquote', wagtail.core.blocks.TextBlock(help_text='Paragraph displays below the subtitle of this block', required=True)), ('mission_card', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('fe-activity', 'Activity'), ('fe-airplay', 'AirPlay'), ('fe-alert-circle', 'Alert Circle'), ('fe-alert-octagon', 'Alert Octagon'), ('fe-alert-triangle', 'Alert Triangle'), ('fe-align-center', 'Align Center'), ('fe-align-justify', 'Align Justify'), ('fe-align-left', 'Align Left'), ('fe-align-right', 'Align Right'), ('fe-anchor', 'Anchor'), ('fe-aperture', 'Aperture'), ('fe-archive', 'Archive'), ('fe-arrow-down-circle', 'Arrow Down Circle'), ('fe-arrow-down-left', 'Arrow Down Left'), ('fe-arrow-down-right', 'Arrow Down Right'), ('fe-arrow-down', 'Arrow Down'), ('fe-arrow-left-circle', 'Arrow Left Circle'), ('fe-arrow-left', 'Arrow Left'), ('fe-arrow-right-circle', 'Arrow Right Circle'), ('fe-arrow-right', 'Arrow Right'), ('fe-arrow-up-circle', 'Arrow Up Circle'), ('fe-arrow-up-left', 'Arrow Up Left'), ('fe-arrow-up-right', 'Arrow Up Right'), ('fe-arrow-up', 'Arrow Up'), ('fe-at-sign', 'At Sign'), ('fe-award', 'Award'), ('fe-bar-chart-2', 'Bar Chart 2'), ('fe-bar-chart', 'Bar Chart'), ('fe-battery-charging', 'Battery Charging'), ('fe-battery', 'Battery'), ('fe-behance', 'Behance'), ('fe-bell-off', 'Bell Off'), ('fe-bell', 'Bell'), ('fe-bluetooth', 'Bluetooth'), ('fe-bold', 'Bold'), ('fe-book-open', 'Open Book'), ('fe-book', 'Book'), ('fe-bookmark', 'Bookmark'), ('fe-box', 'Box'), ('fe-briefcase', 'Briefcase'), ('fe-calendar', 'Calendar'), ('fe-camera-off', 'Camera Off'), ('fe-camera', 'Camera'), ('fe-cast', 'Cast'), ('fe-check-circle', 'Check Circle'), ('fe-check-square', 'Check Square'), ('fe-check', 'Check'), ('fe-chevron-down', 'Chevron Down'), ('fe-chevron-left', 'Chevron Left'), ('fe-chevron-right', 'Chevron Right'), ('fe-chevron-up', 'Chevron Up'), ('fe-chevron-down', 'Chevron Down'), ('fe-chevrons-left', 'Chevrons Left'), ('fe-chevrons-right', 'Chevrons Right'), ('fe-chevrons-up', 'Chevrons Up'), ('fe-chrome', 'Chrome'), ('fe-clipboard', 'Clipboard'), ('fe-clock', 'Clock'), ('fe-cloud-drizzle', 'Cloud Drizzle'), ('fe-cloud-lightning', 'Cloud Lightning'), ('fe-cloud-off', 'Cloud Off'), ('fe-cloud-rain', 'Cloud Rain'), ('fe-cloud-snow', 'Cloud Snow'), ('fe-cloud', 'Cloud'), ('fe-code', 'Code'), ('fe-codepen', 'Codepen'), ('fe-codesandbox', 'Code Sandbox'), ('fe-coffee', 'Coffee'), ('fe-columns', 'Columns'), ('fe-command', 'Command'), ('fe-compass', 'Compass'), ('fe-copy', 'Copy'), ('fe-corner-down-left', 'Corner Down Left'), ('fe-corner-down-right', 'Corner Down Right'), ('fe-corner-left-down', 'Corner Left Down'), ('fe-corner-left-up', 'Corner Left Up'), ('fe-corner-right-down', 'Corner Right Down'), ('fe-corner-right-up', 'Corner Right Up'), ('fe-corner-up-left', 'Corner Up Left'), ('fe-corner-up-right', 'Corner Up Right'), ('fe-cpu', 'CPU'), ('fe-credit-card', 'Credit Card'), ('fe-crop', 'Crop'), ('fe-crosshair', 'Crosshair'), ('fe-database', 'Database'), ('fe-delete', 'Delete'), ('fe-disc', 'Disc'), ('fe-dollar-sign', 'Dollar Sign'), ('fe-download-cloud', 'Download Cloud'), ('fe-download', 'Download'), ('fe-dribbble', 'Dribble'), ('fe-droplet', 'Droplet'), ('fe-edit-2', 'Edit 2'), ('fe-edit-3', 'Edit 3'), ('fe-edit', 'Edit'), ('fe-external-link', 'External Link'), ('fe-eye-off', 'Eye Off'), ('fe-eye', 'Eye'), ('fe-facebook', 'Facebook'), ('fe-fast-forward', 'Fast Forward'), ('fe-feather', 'Feather'), ('fe-figma', 'Figma'), ('fe-file-minus', 'File Minus'), ('fe-file-plus', 'File Plus'), ('fe-file-text', 'File Text'), ('fe-file', 'File'), ('fe-film', 'Film'), ('fe-filter-alt', 'Filter Alt'), ('fe-filter', 'Filter'), ('fe-flag', 'Flag'), ('fe-folder-minus', 'Folder Minus'), ('fe-folder-plus', 'Folder Plus'), ('fe-folder', 'Folder'), ('fe-framer', 'Framer'), ('fe-frown', 'Frown'), ('fe-gift', 'Gift'), ('fe-git-branch', 'Git Branch'), ('fe-git-commit', 'Git Commit'), ('fe-git-merge', 'Git Merge'), ('fe-git-pull-request', 'Git Pull Request'), ('fe-github', 'Github'), ('fe-gitlab', 'Gitlab'), ('fe-globe', 'Globe'), ('fe-google', 'Google'), ('fe-grid', 'Grid'), ('fe-hangouts', 'Hangouts'), ('fe-hard-drive', 'Hard Drive'), ('fe-hash', 'Hash'), ('fe-headphones', 'Headphones'), ('fe-heart', 'Heart'), ('fe-help-circle', 'Help Circle'), ('fe-hexagon', 'Hexagon'), ('fe-home', 'Home'), ('fe-image', 'Image'), ('fe-inbox', 'Inbox'), ('fe-info', 'Info'), ('fe-instagram', 'Instagram'), ('fe-italic', 'Italic'), ('fe-key', 'Key'), ('fe-layers', 'Layers'), ('fe-layout', 'Layout'), ('fe-life-buoy', 'Life Bouy'), ('fe-link-2', 'Link 2'), ('fe-link', 'Link'), ('fe-linkedin', 'Linkedin'), ('fe-list', 'List'), ('fe-loader', 'Loader'), ('fe-lock', 'Lock'), ('fe-log-in', 'Log In'), ('fe-log-out', 'Log Out'), ('fe-mail', 'Mail'), ('fe-map-pin', 'Map Pin'), ('fe-map', 'Map'), ('fe-maximize-2', 'Maximize 2'), ('fe-maximize', 'Maximize'), ('fe-meh', 'Meh'), ('fe-menu', 'Menu'), ('fe-message-circle', 'Message Circle'), ('fe-message-square', 'Message Square'), ('fe-messenger', 'Messenger'), ('fe-mic-off', 'Microphone Mute'), ('fe-mic', 'Microphone'), ('fe-minimize-2', 'Minimize 2'), ('fe-minimize', 'Minimize'), ('fe-minus-circle', 'Minus Circle'), ('fe-minus-square', 'Minus Square'), ('fe-minus', 'Minus'), ('fe-monitor', 'Monitor'), ('fe-moon', 'Moon'), ('fe-more-horizontal', 'More Horizontal'), ('fe-more-vertical', 'More Vertical'), ('fe-mouse-pointer', 'Mouse Pointer'), ('fe-move', 'Move'), ('fe-music', 'Music'), ('fe-navigation-2', 'Navigation 2'), ('fe-navigation', 'Navigation'), ('fe-octagon', 'Octagon'), ('fe-package', 'Package'), ('fe-paperclip', 'Paperclip'), ('fe-pause-circle', 'Pause Circle'), ('fe-pause', 'Pause'), ('fe-paypal', 'PayPal'), ('fe-pen-tool', 'Pen Tool'), ('fe-percent', 'Percent'), ('fe-phone-call', 'Phone Call'), ('fe-phone-forwarded', 'Phone Forwarded'), ('fe-phone-incoming', 'Phone Call Incoming'), ('fe-phone-missed', 'Phone Call Missed'), ('fe-phone-off', 'Phone Off'), ('fe-phone-outgoing', 'Phone Outgoing'), ('fe-phone', 'Phone'), ('fe-pie-chart', 'Pie Chart'), ('fe-pinterest', 'Pinterest'), ('fe-play-circle', 'Play Circle'), ('fe-play', 'Play'), ('fe-plus-circle', 'Plus Circle'), ('fe-plus-square', 'Plus Square'), ('fe-plus', 'Plus'), ('fe-pocket', 'Pocket'), ('fe-power', 'Power'), ('fe-printer', 'Printer'), ('fe-quotes', 'Quotes'), ('fe-radio', 'Radio'), ('fe-refresh-ccw', 'Refresh CCW'), ('fe-refresh-cw', 'Refresh CW'), ('fe-repeat', 'Repeat'), ('fe-rewind', 'Rewind'), ('fe-rotate-ccw', 'Rotate CCW'), ('fe-rotate-cw', 'Rotate CW'), ('fe-rss', 'RSS Feed'), ('fe-save', 'Save'), ('fe-scissors', 'Scissors'), ('fe-search', 'Search'), ('fe-send', 'Send'), ('fe-server', 'Server'), ('fe-settings', 'Settings'), ('fe-share-2', 'Share 2'), ('fe-share', 'Share'), ('fe-shield-off', 'Shield-Off'), ('fe-shield', 'Shield'), ('fe-shopping-bag', 'Shopping Bag'), ('fe-shopping-cart', 'Shopping Cart'), ('fe-shuffle', 'Shuffle'), ('fe-sidebar', 'Sidebar'), ('fe-skip-back', 'Skip Back'), ('fe-skip-forward', 'Skip Forward'), ('fe-skype', 'Skype'), ('fe-slack', 'Slack'), ('fe-slash', 'Slash'), ('fe-sliders', 'Sliders'), ('fe-smartphone', 'Smartphone'), ('fe-smile', 'Smile'), ('fe-speaker', 'Speaker'), ('fe-star', 'Star'), ('fe-stop-circle', 'Stop Circle'), ('fe-sun', 'Sun'), ('fe-sunrise', 'Sunrise'), ('fe-sunset', 'Sunset'), ('fe-tablet', 'Tablet'), ('fe-tag', 'Tag'), ('fe-target', 'Target'), ('fe-telegram', 'Telegram'), ('fe-terminal', 'Terminal'), ('fe-thermometer', 'Thermometer'), ('fe-thumbs-down', 'Thumbs Down'), ('fe-thumbs-up', 'Thumbs Up'), ('fe-toggle-left', 'Toggle Left'), ('fe-toggle-right', 'Toggle Right'), ('fe-tool', 'Tool'), ('fe-trash-2', 'Trash 2'), ('fe-trash', 'Trash'), ('fe-trello', 'Trello'), ('fe-trending-down', 'Trending Down'), ('fe-trending-up', 'Trending Up'), ('fe-truck', 'Truck'), ('fe-tumblr', 'Tumblr'), ('fe-tv', 'TV'), ('fe-twitch', 'Twitch'), ('fe-twitter', 'Twitter'), ('fe-type', 'Type'), ('fe-umbrella', 'Umbrella'), ('fe-underline', 'Underline'), ('fe-unlock', 'Unlock'), ('fe-upload-cloud', 'Upload Cloud'), ('fe-upload', 'Upload'), ('fe-user-check', 'User Check'), ('fe-user-minus', 'User Minus'), ('fe-user-plus', 'User Plus'), ('fe-user-x', 'User X'), ('fe-user', 'User'), ('fe-users', 'Users'), ('fe-viber', 'Viber'), ('fe-video-off', 'Video Off'), ('fe-video', 'Video'), ('fe-vimeo', 'Vimeo'), ('fe-vk', 'VK'), ('fe-voicemail', 'Voicemail'), ('fe-volume-1', 'Volume 1'), ('fe-volume-2', 'Volume 2'), ('fe-volume-x', 'Volume X'), ('fe-volume', 'Volume'), ('fe-watch', 'Watch'), ('fe-wechat', 'WeChat'), ('fe-wifi-off', 'WiFi Off'), ('fe-wifi', 'WiFi'), ('fe-wind', 'Wind'), ('fe-x-circle', 'X Circle'), ('fe-x-octagon', 'X Octagon'), ('fe-x-square', 'X Square'), ('fe-x', 'X'), ('fe-youtube', 'YouTube'), ('fe-zap-off', 'Zap Off'), ('fe-zap', 'Zap'), ('fe-zoom-in', 'Zoom In'), ('fe-zoom-out', 'Zoom Out')])), ('icon_color', wagtail.core.blocks.ChoiceBlock(choices=[('success', 'Green'), ('warning', 'Yellow'), ('danger', 'Red'), ('primary', 'Blue')])), ('text', wagtail.core.blocks.CharBlock(max_length=50, required=True))], icon='fa-handshake-o')))]))])),
                ('content', wagtail.core.fields.StreamField([('doctor_spotlight', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='The Doctor Behind Our Success', max_length=200, required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('qualifications', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('qualification', wagtail.core.blocks.CharBlock(max_length=100, required=True))], icon='fa-university'))), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('testimonials', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='What People Say About Us', max_length=100, required=False))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Schedule a Consultation Today!', max_length=200, required=True)), ('subtitle', wagtail.core.blocks.TextBlock(default="Don't let pain keep you from the activities you love. We would love to help return you to your healthy and active lifestyle!", required=True)), ('button_text', wagtail.core.blocks.CharBlock(default='Schedule Now', max_length=50, required=True)), ('button_link', wagtail.core.blocks.PageChooserBlock(required=True)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('secondary', 'Gray'), ('light', 'White')]))])), ('map', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Restore Orthopedics & Sports Medicine, Dr. Ariana DeMers, DO', max_length=200, required=True)), ('address', wagtail.core.blocks.CharBlock(default='13949 Mono Way, Sonora, CA 95370', max_length=255, required=True)), ('phone_number', wagtail.core.blocks.CharBlock(default='(209) 533 5371', max_length=255, required=True)), ('email', wagtail.core.blocks.EmailBlock(default='admin@restoreorthobiologic.com', max_length=255, required=True)), ('map_link', wagtail.core.blocks.URLBlock(default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3145.0021611358766!2d-120.34119008383189!3d37.977078879722995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8090c528b63b1ba3%3A0xb75939887ae2279d!2sRestore%20Orthopedics%20and%20Sports%20Medicine%3A%20Ariana%20DeMers%2C%20D.O.!5e0!3m2!1sen!2sus!4v1601053197881!5m2!1sen!2sus', max_length=2000, required=True))]))])),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'verbose_name': 'About Page',
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
    ]