sources = [
  'lastfmbot.py'
]

python.install_sources(
  sources,
  subdir: join_paths('calliope_bots/bots/lastfmbot'))

configure_file(
  input: 'lastfmbot.yaml.in',
  output: 'lastfmbot.yaml',
  configuration: cdata,
  install: true,
  install_dir: calliopebotdir)
