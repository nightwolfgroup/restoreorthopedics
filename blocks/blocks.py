from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from wagtail.core import blocks
from wagtail.core.blocks import StructBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

from core.choices import FE_ICONS, CARD_PLACEMENT_CHOICES


# Title Blocks -------------------------------------------------------------------------------------------------------->
class TitleBlock(blocks.StructBlock):
    """ Standard title block with subtitle on gradient background """
    title = blocks.CharBlock(required=True, max_length=50)
    subtitle = blocks.CharBlock(required=False, max_length=100)
    image = ImageChooserBlock(
        required=False,
        help_text='Image displayed behind title text with gradient overlay',
        label='Background Image'
    )

    class Meta:
        template = 'blocks/title_blocks/title-block.html'
        help_text = 'Standard title block with subtitle on gradient background with optional image'
        label = 'Title'
        icon = 'fa-font'


class TitleWithCard(blocks.StructBlock):
    """ Standard title block with subtitle and card on gradient background """
    title = blocks.CharBlock(required=True, max_length=100)
    subtitle = blocks.RichTextBlock(required=True)
    card_title = blocks.TextBlock(required=True, max_length=100)
    card_text = blocks.RichTextBlock(required=True)

    class Meta:
        template = 'blocks/title_blocks/title-with-card.html'
        help_text = 'Page title with gradient background and card'
        label = 'Page Title With Card'
        icon = 'fa-font'


class ParallaxTitle(StructBlock):
    """ Title with multi-layer Parallax effect (used for homepage) """
    title = blocks.CharBlock(
        required=True,
        help_text='Homepage title text',
        default='Restore Your Healthy & Active Lifestyle!'
    )
    buttons = blocks.ListBlock(
        blocks.StructBlock([
            ('button_text', blocks.CharBlock(
                required=False,
                help_text='Text displayed within the button'
            )),
            ('button_link', blocks.PageChooserBlock(
                required=False,
                help_text='Link to page which the button will go to when clicked'
            )),
        ], icon='fa-hand-o-up')
    )
    image = ImageChooserBlock(
        required=True,
        help_text='Main image displayed on the homepage'
    )
    icon_one = ImageChooserBlock(
        required=False,
        help_text='Icon to display next to Doctor name'
    )
    icon_two = ImageChooserBlock(
        required=False,
        help_text='Icon to display next to Doctor name'
    )

    class Meta:
        template = 'blocks/title_blocks/parallax-title.html'
        help_text = 'Title with multi-layer Parallax effect (used for homepage)'
        label = 'Parallax Page Title'
        icon = 'fa-font'


class ParallaxTitleCard(blocks.StructBlock):
    """ Title with multi-layer Parallax effect and card (used on PRP service page) """
    title = blocks.CharBlock(
        required=True,
        help_text='Title text displayed to the left of the parallax image'
    )
    subtitle = blocks.CharBlock(
        required=False,
        help_text='Text displayed beneath the title text'
    )
    card_title = blocks.CharBlock(
        required=False,
        help_text='Text displayed as the title of the card, which appears below the title'
    )
    card_text = blocks.RichTextBlock(
        required=False,
        help_text='Paragraph displayed to the right of the card title, which appears below the title'
    )

    class Meta:
        template = 'blocks/title_blocks/parallax-title-card.html'
        help_text = 'Title with multi-layer Parallax effect and card (used on PRP service page)'
        label = 'Parallax Page Title with Card'
        icon = 'fa-clone'


class MissionStatementBlock(blocks.StructBlock):
    """ Title block with cards set over vector shape (used on About page) """
    title = blocks.CharBlock(
        required=True,
        max_length=30,
        default='Our Commitment to You'
    )
    subtitle = blocks.CharBlock(
        required=True,
        max_length=50,
        default='Our Goals. Our Mission.'
    )
    blockquote = blocks.TextBlock(
        required=True,
        help_text='Paragraph displays below the subtitle of this block'
    )
    mission_card = blocks.ListBlock(
        blocks.StructBlock([
            ('icon', blocks.ChoiceBlock(choices=FE_ICONS)),
            ('icon_color', blocks.ChoiceBlock(
                choices=[
                    ('success', 'Green'),
                    ('warning', 'Yellow'),
                    ('danger', 'Red'),
                    ('primary', 'Blue')
                ]
            )),
            ('text', blocks.CharBlock(max_length=50, required=True))
        ], icon='fa-handshake-o')
    )

    class Meta:
        template = 'blocks/title_blocks/mission-statement.html'
        help_text = 'Title block with cards set over vector shape (used on About page)'
        label = 'About Page Title & Mission Statement'
        icon = 'fa-font'


class CarouselTitle(blocks.StructBlock):
    title = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text='Title displayed to the left of auto-scrolling carousel images'
    )
    subtitle = blocks.CharBlock(
        required=False,
        max_length=1000,
        help_text='Text displayed beneath title'
    )
    button_text = blocks.CharBlock(
        required=False,
        max_length=50,
        help_text='Text displayed in optional button beneath the title'
    )
    button_link = blocks.PageChooserBlock(
        required=False,
        help_text='The page the button will link to'
    )
    carousel_images = blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock(
                required=True,
                help_text='An image displayed inside an auto-scrolling carousel'
            )),
            ('icon', blocks.ChoiceBlock(
                required=False,
                choices=FE_ICONS,
                max_length=30,
                help_text='Optional icon displayed to the left of the image description'
            )),
            ('description', blocks.CharBlock(
                required=False,
                max_length=20,
                help_text='Optional description to display beneath the carousel image'
            ))
        ], icon='fa-picture-o'), label='Image'
    )
    info_icons = blocks.ListBlock(
        blocks.StructBlock([
            ('icon', ImageChooserBlock(
                required=True,
                help_text='Icon displayed below the page title'
            )),
            ('text', blocks.CharBlock(
                required=True,
                max_length=100,
                help_text='Text displayed beneath the icon'
            )),
            ('subtext', blocks.CharBlock(
                required=False,
                max_length=500,
                help_text='Optional text displayed beneath the main text of the icon'
            ))
        ], icon='fa-picture-o'), label='Informational Icons'
    )

    class Meta:
        template = 'blocks/title_blocks/carousel-title.html'
        help_text = 'Title block with auto-scrolling images and optional button'
        label = 'Carousel Title'
        icon = 'fa-picture-o'


# CTA Blocks ---------------------------------------------------------------------------------------------------------->
class CTABlock(blocks.StructBlock):
    """ CTA Block with icon links set over white circles """
    title = blocks.CharBlock(max_length=100, required=True)
    subtitle = blocks.TextBlock(required=True)
    link = blocks.ListBlock(
        blocks.StructBlock([
            ('icon', ImageChooserBlock(required=True)),
            ('link_text', blocks.CharBlock(required=True)),
            ('link', blocks.PageChooserBlock(required=True))
        ], icon='fa-link')
    )
    background_image = ImageChooserBlock(required=False)

    class Meta:
        template = 'blocks/cta_blocks/new-patient-cta.html'
        help_text = 'CTA Block with icon links set over white circles'
        label = 'Call to Action'
        icon = 'fa-bullhorn'


class CTALogoBlock(blocks.StructBlock):
    """ Branded CTA Block with button """
    title = blocks.CharBlock(
        max_length=200,
        required=True,
        default='Schedule a Consultation Today!'
    )
    subtitle = blocks.TextBlock(
        required=True,
        default="Don't let pain keep you from the activities you love. "
                "We would love to help return you to your healthy and active lifestyle!"
    )
    button_text = blocks.CharBlock(
        max_length=50,
        required=True,
        default='Schedule Now'
    )
    button_link = blocks.PageChooserBlock(required=True)
    background_color = blocks.ChoiceBlock(required=True, choices=[('secondary', 'Gray'), ('light', 'White')])

    class Meta:
        template = 'blocks/cta_blocks/cta-with-button.html'
        help_text = 'Branded CTA Block With Button'
        label = 'CTA With Logo & Button'
        icon = 'fa-bullhorn'


# Content Blocks ------------------------------------------------------------------------------------------------------>
class ServiceCards(blocks.StructBlock):
    """ Cards with icon, title, and text set over a vector shape """
    title = blocks.CharBlock(
        required=True,
        help_text='Section title',
        default='Our services'
    )
    subtitle = blocks.CharBlock(
        required=False,
        help_text='Text displayed beneath title'
    )
    card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('Icon', ImageChooserBlock(required=True)),
                ('Title', blocks.CharBlock(max_length=50, required=True)),
                ('Description', blocks.TextBlock(max_length=255, required=True))
            ], icon='fa-medkit'
        )
    )

    class Meta:
        template = 'blocks/content_blocks/services-cards.html'
        help_text = 'Cards with icon, title, and text (set over vector shape)'
        label = 'Service Cards'
        icon = 'fa-tag'


class ServicesTitleBlock(blocks.StructBlock):
    subtitle = blocks.CharBlock(
        required=False,
        help_text='Optional subtitle to display below the page title',
    )
    background_image = ImageChooserBlock(
        required=False,
        help_text='Optional image to display behind the title and services carousel with gradient overlay'
    )
    service = blocks.ListBlock(
        blocks.StructBlock([
            ('icon', ImageChooserBlock(required=False, help_text='Optional icon displayed above the service title')),
            ('name', blocks.CharBlock(max_length=30, required=True, help_text='Service name displayed in the card')),
            ('description',
             blocks.TextBlock(required=False, help_text='Service description displayed below the service title')),
            ('image', ImageChooserBlock(required=True, help_text='Image displayed behind the service card')),
            ('link_text', blocks.CharBlock(max_length=30, required=False,
                                           help_text='Optional link: this text will display as a link')),
            ('link', blocks.PageChooserBlock(required=False, help_text='Page the link text will to link to'))
        ], icon='fa-medkit')
    )

    class Meta:
        template = 'blocks/content_blocks/services.html'
        label = 'Services Page Title'
        icon = 'fa-tag'


class MapBlock(blocks.StructBlock):
    """ Google Map block with non-global contact information """
    title = blocks.CharBlock(
        required=True,
        max_length=200,
        default='Restore Orthopedics & Sports Medicine, Dr. Ariana DeMers, DO'
    )
    address = blocks.CharBlock(
        required=True,
        max_length=255,
        default='13949 Mono Way, Sonora, CA 95370'
    )
    phone_number = blocks.CharBlock(
        required=True,
        max_length=255,
        default='(209) 533 5371'
    )
    email = blocks.EmailBlock(
        required=True,
        max_length=255,
        default='admin@restoreorthobiologic.com'
    )
    map_link = blocks.URLBlock(
        max_length=2000,
        required=True,
        default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3145.0021611358766!2d-120.34119008383189!3d37.'
                '977078879722995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8090c528b63b1ba3%3A0xb75939887ae'
                '2279d!2sRestore%20Orthopedics%20and%20Sports%20Medicine%3A%20Ariana%20DeMers%2C%20D.O.!5e0!3m2!1sen!'
                '2sus!4v1601053197881!5m2!1sen!2sus'
    )

    class Meta:
        template = 'blocks/content_blocks/map.html'
        help_text = 'Interactive Google Map with contact information'
        label = 'Map with Contact Info'
        icon = 'fa-map'


class DoctorSpotlight(blocks.StructBlock):
    title = blocks.CharBlock(
        required=True,
        max_length=200,
        default='The Doctor Behind Our Success'
    )
    text = blocks.TextBlock(
        required=True
    )
    qualifications = blocks.ListBlock(
        blocks.StructBlock([
            ('qualification', blocks.CharBlock(max_length=100, required=True))
        ], icon='fa-university')
    )
    image = ImageChooserBlock(required=True)

    class Meta:
        template = 'blocks/content_blocks/doctor-spotlight.html'
        icon = 'fa-user'
        label = 'Doctor Spotlight with Image'


class JarallaxImage(blocks.StructBlock):
    image_1 = ImageChooserBlock(
        required=True,
        help_text='Large rounded image displayed next to text'
    )
    title_1 = blocks.CharBlock(
        required=True,
        max_length=30,
        help_text='Title for image 1'
    )
    text_1 = blocks.TextBlock(
        required=True,
        help_text='Text displayed beneath the title'
    )
    list_1 = blocks.ListBlock(
        blocks.StructBlock([
            ('item', blocks.CharBlock(required=False, help_text='Bulleted item list displayed beneath text'))
        ], icon='fa-list-ul')
    )
    image_2 = ImageChooserBlock(
        required=True,
        help_text='Large rounded image displayed next to text'
    )
    title_2 = blocks.CharBlock(
        required=True,
        max_length=30,
        help_text='Title for image 2'
    )
    text_2 = blocks.TextBlock(
        required=True,
        help_text='Text displayed beneath the title'
    )
    list_2 = blocks.ListBlock(
        blocks.StructBlock([
            ('item', blocks.CharBlock(required=False, help_text='Bulleted item list displayed beneath text'))
        ], icon='fa-list-ul')
    )

    class Meta:
        template = 'blocks/content_blocks/jarallax-image-with-text.html'
        icon = 'fa-image'
        label = '2 Images with Text and List'


class HotspotsBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        required=True,
        max_length=50,
        help_text='Title displayed above image'
    )
    image = ImageChooserBlock(
        required=True,
        help_text='Image to display with hostpots overlay'
    )
    hotspots = blocks.ListBlock(
        blocks.StructBlock([
            ('card_title', blocks.CharBlock(
                required=True
            )),
            ('card_text', blocks.TextBlock(
                required=True
            )),
            ('card_placement', blocks.ChoiceBlock(
                required=True,
                choices=CARD_PLACEMENT_CHOICES,
                help_text='Location of card upon hover of hotspot'
            )),
            ('x_axis', blocks.IntegerBlock(required=True, help_text='Horizontal Placement (%)')),
            ('y_axis', blocks.IntegerBlock(required=True, help_text='Vertical Placement (%)'))
        ], icon='fa-plus-circle')
    )

    class Meta:
        template = 'blocks/content_blocks/hotspots.html'
        icon = 'fa-fire'
        label = 'Hotspots Image'


class IconList(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=100)
    item = blocks.ListBlock(
        blocks.StructBlock([
            ('icon', ImageChooserBlock(required=True)),
            ('title', blocks.CharBlock(required=True, max_length=20)),
            ('list', blocks.ListBlock(
                blocks.StructBlock([
                    ('item', blocks.CharBlock(required=True, max_length=30))
                ], icon='fa-check-circle-o')
            ))
        ], icon='fa-list-ul')
    )

    class Meta:
        template = 'blocks/content_blocks/iconlist.html'
        icon = 'fa-ellipsis-h'
        label = 'Icons with Bulleted List'


class IconCardWithLink(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100, required=False, help_text='Optional title to display above cards')
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ('icon', blocks.ChoiceBlock(
                required=False,
                choices=FE_ICONS,
                max_length=20,
                help_text='Icon to display at top of card'
            )),
            ('title', blocks.CharBlock(
                required=True,
                max_length=30,
                help_text='Card Title'
            )),
            ('text', blocks.CharBlock(
                required=True,
                max_length=200,
                help_text='Card Text'
            )),
            ('button_text', blocks.CharBlock(
                required=True,
                max_length=50,
                default='Learn more'
            )),
            ('button_link', blocks.PageChooserBlock(
                required=True
            ))
        ], icon='fa-clone')
    )

    class Meta:
        template = 'blocks/content_blocks/cards-icon-link.html'
        icon = 'fa-clone'
        label = 'Cards with Icon & Button'


class HelpBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        required=True,
        max_length=100,
        default="Haven't found the answer? We can help."
    )
    button_text = blocks.CharBlock(
        required=True,
        max_length=50,
        default='Send us a Message'
    )
    button_link = blocks.PageChooserBlock(
        required=True
    )
    subtext = blocks.CharBlock(
        required=True,
        max_length=200,
        default='Contact us and we’ll get back to you as soon as possible.'
    )
    background_color = blocks.ChoiceBlock(
        required=True,
        choices=[('secondary', 'Light Gray'), ('light', 'White')],
        default='secondary'
    )

    class Meta:
        template = 'blocks/content_blocks/help-block.html'
        icon = 'fa-life-ring'
        label = 'Help Block'
        help_text = 'Help Block with Contact Button'


class GalleryModalBlock(blocks.StructBlock):
    card = blocks.ListBlock(
        blocks.StructBlock([
            ('title', blocks.CharBlock(
                required=True,
                max_length=100,
                help_text='Text displayed below the card image'
            )),
            ('image', ImageChooserBlock(
                required=True,
                help_text='Full size image for the pop-up modal'
            )),
        ], icon='fa-window-maximize')
    )

    class Meta:
        template = 'blocks/content_blocks/gallery-modal-block.html'
        label = 'Card Image & Modal Pop-Up'
        help_text = 'Card with thumbnail image and title, when clicked, a pop-up will display the full-size image'
        icon = 'fa-window-restore'


class GalleryFileDownloadBlock(blocks.StructBlock):
    card = blocks.ListBlock(
        blocks.StructBlock([
            ('title', blocks.CharBlock(
                required=True,
                max_length=35,
                help_text='Text displayed below the card image'
            )),
            ('subtitle', blocks.CharBlock(
                required=False,
                max_length=100,
                help_text='Text displayed below the card title, can be used to place an author name below an eBook'
            )),
            ('thumbnail', ImageChooserBlock(
                required=True,
                help_text='Thumbnail preview of linked file'
            )),
            ('file', DocumentChooserBlock(
                required=False,
                help_text='File (such as an eBook, to download when card is clicked)'
            ))
        ], icon='fa-file')
    )

    class Meta:
        template = 'blocks/content_blocks/gallery-file-download-cards.html'
        label = 'Card Thumbnail with Linked File'
        help_text = 'Card with thumbnail image and title, when clicked, linked file will download'
        icon = 'fa-book'


class VideoShowcaseBlock(blocks.StructBlock):
    videos = blocks.ListBlock(
        blocks.StructBlock([
            ('title', blocks.CharBlock(
                required=True,
                max_length=200,
                help_text='Video Title'
            )),
            ('link', blocks.URLBlock(
                required=True,
                help_text='Video URL (from YouTube, Vimeo, etc.)'
            )),
            ('thumbnail', ImageChooserBlock(
                required=True,
                help_text='Video Thumbnail'
            ))
        ], icon='fa-play')
    )

    class Meta:
        template = 'blocks/content_blocks/video-showcase.html'
        label = 'Video Showcase'
        icon = 'fa-play'


class ImageIconList(blocks.StructBlock):
    image = ImageChooserBlock(
        required=True,
        help_text='Image displayed to the left of section content. Will be video icon if a video URL is provided.'
    )
    title = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text='Block title',
    )
    subtitle = blocks.TextBlock(
        required=False,
        help_text='Optional text to display below the block title'
    )
    video_url = blocks.URLBlock(
        required=False,
        help_text='Optional Video URL, will create a play button over the block image. '
                  'Video will play in a pop-up window.'
    )
    list_items = blocks.ListBlock(
        blocks.StructBlock([
            ('icon', ImageChooserBlock(
                required=False,
                help_text='Optional icon to display next to the list item'
            )),
            ('title', blocks.CharBlock(
                required=True,
                max_length=255,
                help_text='Title of list item displayed below the main title'
            )),
            ('subtitle', blocks.CharBlock(
                required=False,
                max_length=1000,
                help_text='Optional text displayed below the list item title'
            ))
        ], icon='fa-list-ul'), label='List element with icon'
    )

    class Meta:
        template = 'blocks/content_blocks/image-icon-bulleted-list.html'
        label = 'Image With Icon Bulleted List'
        icon = 'fa-list-ul'
        help_text = 'Large image displayed on the left/right of custom icon bulleted list'


# Testimonial Blocks -------------------------------------------------------------------------------------------------->
class TestimonialCards(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        required=False,
        default='What People Say About Us'
    )

    def get_context(self, request, *args, **kwargs):
        from core.snippets import Testimonial
        context = super().get_context(request, *args, **kwargs)
        testimonials = Testimonial.objects.all()
        context['testimonials'] = testimonials
        return context

    class Meta:
        template = 'blocks/testimonial_blocks/testimonials.html'
        label = 'Testimonial Cards'
        icon = 'openquote'


class TestimonialIllustration(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        required=False,
        default='What People Say About Us'
    )

    def get_context(self, request, *args, **kwargs):
        from core.snippets import Testimonial
        context = super().get_context(request, *args, **kwargs)
        testimonials = Testimonial.objects.all()
        context['testimonials'] = testimonials
        return context

    class Meta:
        template = 'blocks/testimonial_blocks/testimonials-illustration.html'
        label = 'Testimonial w/ Illustration'
        icon = 'openquote'


class FeaturedTestimonials(blocks.StructBlock):
    title = blocks.CharBlock(max_length=50, required=True, default='Featured Review')
    testimonials = blocks.ListBlock(
        blocks.StructBlock([
            ('testimonial', SnippetChooserBlock('core.Testimonial'))
        ], icon='fa-quote-right')
    )

    class Meta:
        template = 'blocks/testimonial_blocks/featured-testimonial.html'
        label = 'Featured Testimonial'
        icon = 'fa-star'


# FAQ Blocks ---------------------------------------------------------------------------------------------------------->
class CardsWithFAQ(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=100, default='Patient Resources')
    card = blocks.ListBlock(
        blocks.StructBlock([
            ('icon', ImageChooserBlock(required=True)),
            ('title', blocks.CharBlock(max_length=100, required=True)),
            ('subtitle', blocks.TextBlock(required=True)),
            ('link', blocks.PageChooserBlock(required=True)),
            ('link_text', blocks.CharBlock(required=True, max_length=100))
        ], icon='fa-tag')
    )
    faq = blocks.ListBlock(
        blocks.StructBlock([
            ('question', blocks.CharBlock(max_length=255, required=True)),
            ('answer', blocks.RichTextBlock(required=True)),
            ('question_number', blocks.IntegerBlock(required=True))
        ], icon='fa-question'),
        label='Frequently Asked Questions'
    )

    class Meta:
        template = 'blocks/faq_blocks/cards-with-faq.html'
        label = 'Cards with FAQ'
        icon = 'fa-tag'


class FAQBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=50, required=True, help_text='Title of FAQ list')
    related_articles = blocks.ListBlock(
        blocks.StructBlock([
            ('related_article_name', blocks.CharBlock(required=False, max_length=100)),
            ('related_article_link', blocks.PageChooserBlock(required=False))
        ], icon='fa-window-restore'), label='Related Articles'
    )
    faq = blocks.ListBlock(
        blocks.StructBlock([
            ('question', blocks.CharBlock(max_length=255, required=True)),
            ('answer', blocks.RichTextBlock(required=True))
        ], icon='fa-question'),
        label='Frequently Asked Questions'
    )

    class Meta:
        template = 'blocks/faq_blocks/faq-page-block.html'
        label = 'FAQ Block (Full Page)'
        icon = 'fa-question'


# Blog Blocks --------------------------------------------------------------------------------------------------------->
class LatestBlogPosts(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        required=True,
        default='Our Blog'
    )

    class Meta:
        template = 'blocks/content_blocks/latest-blog-posts.html'
        label = 'Latest Blog Posts'
        icon = 'fa-rss'

    def get_context(self, request, *args, **kwargs):
        from blog.models import BlogPost
        context = super().get_context(request, *args, **kwargs)
        posts = BlogPost.objects.live().public().order_by('-first_published_at')[:5:1]
        context['posts'] = posts
        return context


# Legal Page Blocks --------------------------------------------------------------------------------------------------->
class LegalBlock(blocks.StructBlock):
    page_content = blocks.RichTextBlock(required=True)
    related_articles = blocks.ListBlock(
        blocks.StructBlock([
            ('related_article_name', blocks.CharBlock(required=False, max_length=100)),
            ('related_article_link', blocks.PageChooserBlock(required=False))
        ], icon='fa-window-restore'), label='Related Articles'
    )

    class Meta:
        template = 'blocks/content_blocks/legal-block.html'
        label = 'Legal Block (Full Page)'
        icon = 'fa-gavel'


# Event Blocks -------------------------------------------------------------------------------------------------------->
class EventTitle(blocks.StructBlock):
    background_image = ImageChooserBlock(
        required=False,
        help_text='Optional Event Title Background Image, if not provided, a gradient background will be present'
    )
    cover_image = ImageChooserBlock(
        required=False,
        help_text='Optional Event Cover Image (Displays Below the Title)'
    )
    button_text = blocks.CharBlock(
        required=True,
        max_length=50,
        help_text='Text displayed inside the button',
        default='Reserve Your Seat'
    )
    button_link = blocks.URLBlock(
        required=True,
        help_text='Eventbrite Link'
    )

    class Meta:
        template = 'blocks/event_blocks/event-title.html'
        label = 'Event Title'
        icon = 'fa-title'


class EventCountdown(blocks.StructBlock):
    countdown_title = blocks.CharBlock(
        required=True,
        help_text='Text to display to the left of the countdown. '
                  'The countdown will automatically update from the event date.',
        default='Event will start in:'
    )

    class Meta:
        template = 'blocks/event_blocks/event-countdown.html'
        label = 'Event Countdown'
        icon = 'fa-clock-o'


class EventSpeakers(blocks.StructBlock):
    speaker = blocks.ListBlock(
        blocks.StructBlock([
            ('name', blocks.CharBlock(
                required=True,
                max_length=255,
                help_text='Speaker Name'
            )),
            ('about', blocks.CharBlock(
                required=False,
                max_length=255,
                help_text="Optional text to display below the speaker's name"
            )),
            ('image', ImageChooserBlock(
                required=True,
                help_text='Speaker Image'
            ))
        ], icon='fa-user'), label='Event Speaker'
    )

    class Meta:
        template = 'blocks/event_blocks/event-speakers.html'
        label = 'Event Speakers'
        icon = 'fa-users'


class EventCTA(blocks.StructBlock):
    image = ImageChooserBlock(
        required=True,
        help_text='Image displayed to the left of CTA content. Will be video icon if a video URL is provided.'
    )
    title = blocks.CharBlock(
        required=True,
        max_length=255,
        help_text='Event CTA Title',
        default='Why you should join the event?'
    )
    video_url = blocks.URLBlock(
        required=False,
        help_text='Optional Video URL, will create a play button over the title image. '
                  'Video will play in a pop-up window.'
    )
    list_items = blocks.ListBlock(
        blocks.StructBlock([
            ('icon', ImageChooserBlock(
                required=False,
                help_text='Optional icon to display next to the list item'
            )),
            ('title', blocks.CharBlock(
                required=True,
                max_length=255,
                help_text='Title for list item displayed below the main title'
            )),
            ('subtitle', blocks.CharBlock(
                required=False,
                max_length=1000,
                help_text='Optional text displayed below the list item title'
            ))
        ], icon='fa-list-ul'), label='CTA Item List'
    )

    class Meta:
        template = 'blocks/event_blocks/event-cta.html'
        label = 'Event CTA'
        icon = 'fa-bullhorn'


class EventStats(blocks.StructBlock):
    statistics = blocks.ListBlock(
        blocks.StructBlock([
            ('number', blocks.IntegerBlock(
                required=True,
                help_text='Number displayed above the statistic'
            )),
            ('statistic', blocks.CharBlock(
                required=True,
                help_text='Statistic name that is displayed below the number'
            ))
        ], icon='fa-hashtag'), label='Event Statistic'
    )

    class Meta:
        template = 'blocks/event_blocks/event-stats.html'
        label = 'Event Statistics'
        icon = 'fa-hashtag'


class EventSchedule(blocks.StructBlock):
    schedule_blocks = blocks.ListBlock(
        blocks.StructBlock([
            ('start_time', blocks.TimeBlock(required=True, help_text='Schedule block start time')),
            ('end_time', blocks.TimeBlock(required=True, help_text='Schedule block end time')),
            ('events', blocks.ListBlock(
                blocks.StructBlock([
                    ('title', blocks.CharBlock(
                        required=True,
                        max_length=500,
                        help_text='Title of what is happening in this schedule block'
                    )),
                    ('subtitle', blocks.CharBlock(
                        required=False,
                        max_length=1000,
                        help_text='Small text displayed above the schedule block title'
                    )),
                    ('speaker_name', blocks.CharBlock(
                        required=False,
                        help_text='If this schedule block features a speaker, you may append their name here'
                    )),
                    ('speaker_image', ImageChooserBlock(
                        required=False,
                        help_text='If adding a speaker name, you may add the speaker image here.'
                    ))
                ], icon='fa-clock-o'), label='Event', help_text='You may add multiple events for each scheduling block'
            ))
        ], icon='fa-clock-o'), label='Event Schedule Block'
    )

    class Meta:
        template = 'blocks/event_blocks/event-schedule.html'
        label = 'Event Schedule'
        icon = 'fa-clock-o'
        help_text = 'Blocks include start and end time with optional speaker name and image for each block'


class EventLocation(blocks.StructBlock):
    title = blocks.CharBlock(
        required=True,
        max_length=50,
        default='Location'
    )
    subtitle = blocks.CharBlock(
        required=False,
        max_length=2000,
        help_text='Optional subtext displayed below the section title, '
                  'may be useful to provide directions to the event location'
    )
    amenities = blocks.ListBlock(
        blocks.StructBlock([
            ('amenity', blocks.CharBlock(required=False, max_length=50))
        ], icon='fa-star'), label='Location Amenities'
    )
    map_image = ImageChooserBlock(required=False)
    map_link = blocks.CharBlock(
        max_length=5000,
        required=False,
        help_text='Google Map Embed Link',
        default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3145.0021611358766!2d-120.34119008383189!'
                '3d37.977078879722995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8090c528b63b1ba3%3A0xb'
                '75939887ae2279d!2sRestore%20Orthopedics%20and%20Sports%20Medicine%3A%20Ariana%20DeMers%2C%20D.O.'
                '!5e0!3m2!1sen!2sus!4v1601053197881!5m2!1sen!2sus'
    )
    location_images = blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock(required=False)),
            ('title', blocks.CharBlock(required=True, max_length=100))
        ], icon='fa-building'), label='Location Images', max_count=4
    )

    class Meta:
        template = 'blocks/event_blocks/event-location.html'
        label = 'Event Location'
        icon = 'fa-building'


class EventTickets(blocks.StructBlock):
    title = blocks.CharBlock(
        required=True,
        max_length=100,
        default='Reserve Your Seat'
    )
    ticket_types = blocks.ListBlock(
        blocks.StructBlock([
            ('name', blocks.CharBlock(
                required=True,
                max_length=255,
                help_text='Name of the type of ticket offered', default='General Admission'
            )),
            ('description', blocks.CharBlock(
                required=False,
                max_length=255,
                help_text='Optional text to further describe the ticket'
            )),
            ('button_text', blocks.CharBlock(
                required=True,
                max_length=50,
                help_text='Text that will display inside the button',
                default='Reserve Your Seat'
            )),
            ('button_link', blocks.URLBlock(
                required=True,
                help_text='Link the button will navigate to when clicked, this should be the Eventbrite page'
            ))
        ], icon='fa-ticket'), label='Ticket Types'
    )

    class Meta:
        template = 'blocks/event_blocks/event-tickets.html'
        label = 'Event Tickets'
        icon = 'fa-ticket'


# Patient Resource Blocks --------------------------------------------------------------------------------------------->
class PDFFormsBlock(blocks.StructBlock):
    forms = blocks.ListBlock(
        blocks.StructBlock([
            ('title', blocks.CharBlock(required=True, max_length=255, help_text='Form title')),
            ('description', blocks.CharBlock(required=False, max_length=500, help_text='Optional form description')),
            ('form', DocumentChooserBlock(required=True, help_text='PDF Form'))
        ], icon='fa-file-text'), label='Form'
    )

    class Meta:
        template = 'blocks/content_blocks/pdf-forms.html'
        label = 'Patient Forms'
        icon = 'fa-file-text'
