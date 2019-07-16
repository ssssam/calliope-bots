project('calliope-bots',
        meson_version: '>= 0.51')

pymod = import('python')

python = pymod.find_installation('python3', modules: ['calliope', 'click', 'yaml'])

if not python.language_version().version_compare('>= 3.5')
  error('Python 3.5 or newer is required.')
endif

calliopebotdir = join_paths(get_option('prefix'), get_option('datadir'), 'calliope-bots', 'bots')

cdata = configuration_data()
cdata.set('calliopebotdir', calliopebotdir)
cdata.set('pythonsitepackagesdir', python.get_install_dir(pure: false))

subdir('bots')
subdir('cli')
