project('calliope-bots',
        meson_version: '>= 0.51')

pymod = import('python')

python = pymod.find_installation('python3', modules: ['calliope', 'click'])

if not python.language_version().version_compare('>= 3.5')
  error('Python 3.5 or newer is required.')
endif

subdir('bots')
