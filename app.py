from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/applications/')
def applications():
    data = [
        {
            'name': 'Material Notes',
            'logo': 'https://cookicons.co/images/app-icons/materialnotes.png',
            'url': 'https://play.google.com/store/apps/details?id=com.dinosaur.cwfei.materialnotes'
        },
        {
            'name': 'Quicklyric',
            'logo': 'https://cookicons.co/images/app-icons/quicklyric.png',
            'url': 'https://github.com/QuickLyric/QuickLyric'
        },
        {
            'name': 'Slide for Reddit',
            'logo': 'https://cookicons.co/images/app-icons/slide.png',
            'url': 'https://plus.google.com/116106540603389817500'
        },
        {
            'name': 'Monospace',
            'logo': 'https://cookicons.co/images/app-icons/monospace.png',
            'url': 'https://plus.google.com/communities/108848211751613632777'
        },
        {
            'name': 'Cinnamon Shopping List',
            'logo': 'https://cookicons.co/images/app-icons/cinnamon.png',
            'url': 'https://play.google.com/store/apps/details?id=com.imdevgary.cinnamon&hl=en'
        },
        {
            'name': 'BE Trains',
            'logo': 'https://cookicons.co/images/app-icons/betrains.png',
            'url': 'https://play.google.com/store/apps/details?id=tof.cv.mpp&hl=en'
        },
        {
            'name': 'Periodic Table',
            'logo': 'https://cookicons.co/images/app-icons/periodictable.png',
            'url': 'https://play.google.com/store/apps/details?id=jqsoft.apps.periodictable.hd&hl=en'
        },
        {
            'name': 'divvyDOSE',
            'logo': 'https://cookicons.co/images/app-icons/divvydose.png',
            'url': 'https://www.divvydose.com/'
        },
        {
            'name': 'Reverse Dictionary',
            'logo': 'https://cookicons.co/images/app-icons/reverse-dictionary.png',
            'url': 'https://play.google.com/store/apps/details?id=tr.philon.redictionary&hl=en'
        },
        {
            'name': 'Book Dash',
            'logo': 'https://cookicons.co/images/app-icons/book-dash.png',
            'url': 'https://play.google.com/store/apps/details?id=org.bookdash.android&hl=en'
        },
        {
            'name': '365 Body Workout',
            'logo': 'https://cookicons.co/images/app-icons/365-body-workout.png',
            'url': 'https://play.google.com/store/apps/details?id=com.peirr.workout.play&hl=en'
        },
        {
            'name': 'Digical',
            'logo': 'https://cookicons.co/images/app-icons/digical.png',
            'url': 'https://play.google.com/store/apps/details?id=com.digibites.calendar'
        },
        {'name': 'Figma Remake', 'logo': 'https://cookicons.co/images/app-icons/figma.png',
         'url': 'https://www.figma.com/'},
        {'name': 'Atomic.io Remake', 'logo': 'https://cookicons.co/images/app-icons/atomic.png',
         'url': 'https://atomic.io/'},
        {
            'name': 'Insight',
            'logo': 'https://cookicons.co/images/app-icons/insight.png',
            'url': 'https://play.google.com/store/apps/details?id=com.bunemekyakilika.insight'
        },
        {
            'name': 'EarlyBird - News for Android',
            'logo': 'https://cookicons.co/images/app-icons/earlybird.png',
            'url': 'https://play.google.com/store/apps/details?id=com.androidforums.earlybird'
        },
        {
            'name': 'App Promos',
            'logo': 'https://cookicons.co/images/app-icons/app-promos.png',
            'url': 'https://play.google.com/store/apps/details?id=com.underwood.promo'
        },
        {
            'name': 'Tickbox',
            'logo': 'https://cookicons.co/images/app-icons/tickbox.png',
            'url': 'https://play.google.com/store/apps/details?id=com.sofaking.list.app'
        },
        {'name': 'Periodex', 'logo': 'https://cookicons.co/images/app-icons/periodex.png',
         'url': 'https://periodex.co/'},
        {
            'name': 'Game of Life',
            'logo': 'https://cookicons.co/images/app-icons/game-of-life.png',
            'url': 'https://play.google.com/store/apps/details?id=com.favpix.gameoflife'
        },
        {
            'name': 'SD Maid',
            'logo': 'https://cookicons.co/images/app-icons/sd-maid.png',
            'url': 'https://play.google.com/store/apps/details?id=eu.thedarken.sdm'
        },
        {
            'name': 'Compass',
            'logo': 'https://cookicons.co/images/app-icons/compass.png',
            'url': 'https://play.google.com/store/apps/details?id=org.tndata.android.compass'
        },
    ]
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
