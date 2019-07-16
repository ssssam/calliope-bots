sources = [
  'peelbot.py',
  'peel-artists-rateyourmusic.json',
]

python.install_sources(
  sources,
  subdir: join_paths('calliope_bots/bots/peelbot'))

configure_file(
  input: 'peelbot.yaml.in',
  output: 'peelbot.yaml',
  configuration: cdata,
  install: true,
  install_dir: calliopebotdir)
