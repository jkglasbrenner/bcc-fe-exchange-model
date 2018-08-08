# pandoc_reader

> A pandoc [markdown] reader plugin for [pelican].

## Requirements

*   [pandoc] in $PATH

## Installation

Instructions for installation of pelican plugins can be obtained from the [pelican plugin manual](https://github.com/getpelican/pelican-plugins/blob/master/Readme.rst).

## Configuration

Additional command line parameters can be passed to pandoc via the PANDOC_ARGS parameter.

```python
PANDOC_ARGS = [
  '--mathjax',
  '--smart',
  '--toc',
  '--toc-depth=2',
  '--number-sections',
]
```

Pandoc's markdown extensions can be enabled or disabled via the
PANDOC_EXTENSIONS parameter.

```python
PANDOC_EXTENSIONS = [
  '+hard_line_breaks',
  '-citations'
]
```

## Contributing

1.  Fork it
    
2.  Create your feature branch (`git checkout -b my-new-feature`)
    
3.  Commit your changes (`git commit -am 'Add some feature'`)
    
4.  Push to the branch (`git push origin my-new-feature`)
    
5.  Create new Pull Request

## License

This plugin is released under the [GNU AFFERO GENERAL PUBLIC LICENSE](./LICENSE).

[markdown]: http://daringfireball.net/projects/markdown/
[pandoc]: http://johnmacfarlane.net/pandoc/
[pelican]: http://getpelican.com
