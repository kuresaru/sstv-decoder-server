"""Parsing arguments and starting program from command line"""

from .decode import SSTVDecoder
from sys import exit
import argparse


class SSTVCommand(object):
    """ Main class to handle the command line features """

    examples_of_use = """
examples:
  Decode local SSTV audio file named 'audio.ogg' to 'result.png':
    $ sstv -d audio.ogg

  Decode SSTV audio file in /tmp to './image.jpg':
    $ sstv -d /tmp/signal.wav -o ./image.jpg
"""

    def __init__(self):
        """ Handle command line arguments """
        self._audio_file = None
        self._output_file = None

        self.args = self.parse_args()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self.close()

    def __del__(self):
        self.close()

    def init_args(self):
        """ Initialise argparse parser """
        version = "sstv 0.1"

        parser = argparse.ArgumentParser(
            prog="sstv",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=self.examples_of_use)

        parser.add_argument("-d", "--decode", type=argparse.FileType('rb'),
                            help="SSTV audio file to decode",
                            dest="audio_file")
        parser.add_argument("-o", "--output", type=argparse.FileType('wb'),
                            help="desination of output file",
                            default="result.png",
                            dest="output_file")
        parser.add_argument("-V", "--version", action="version",
                            version=version)
        parser.add_argument("-v", "--verbose", action="count", default=1,
                            help="increase output to the terminal")
        parser.add_argument("--list-modes", action="store_true",
                            dest="list_modes",
                            help="list supported SSTV modes")
        parser.add_argument("--list-audio-formats", action="store_true",
                            dest="list_audio_formats",
                            help="list supported audio file formats")
        parser.add_argument("--list-image-formats", action="store_true",
                            dest="list_image_formats",
                            help="list supported image file formats")
        return parser

    def parse_args(self):
        """ Parse command line arguments """
        parser = self.init_args()
        args = parser.parse_args()

        self._audio_file = args.audio_file
        self._output_file = args.output_file

        if args.list_modes:
            self.list_supported_modes()
            exit(0)
        if args.list_audio_formats:
            self.list_supported_audio_formats()
            exit(0)
        if args.list_image_formats:
            self.list_supported_image_formats()
            exit(0)

        if self._audio_file is None:
            parser.print_help()
            exit(2)

        return args

    def start(self):
        with SSTVDecoder(self._audio_file) as sstv:
            img = sstv.decode()
            try:
                img.save(self._output_file)
            except KeyError:
                img.save("result.png")

    def close(self):
        """ Closes any input/output files if they exist """
        if self._output_file is not None and not self._output_file.closed:
            self._output_file.close()
        if self._audio_file is not None and not self._audio_file.closed:
            self._audio_file.close()

    def list_supported_modes(self):
        # FIXME hardcode
        print("M1, S1")

    def list_supported_audio_formats(self):
        # FIXME hardcode
        print("ogg, wav")

    def list_supported_image_formats(self):
        # FIXME hardcode
        print("png, jpeg")
