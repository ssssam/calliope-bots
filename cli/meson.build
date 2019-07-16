sources = files(
  '__main__.py',
)

python.install_sources(
    sources,
    pure: false,
    subdir: join_paths('calliope_bots', 'cli'))

configure_file(
    input: 'main.py.in',
    output: 'calliope-bots-cli',
    configuration: cdata,
    install_dir: get_option('bindir'))
