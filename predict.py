import os
import sys
import shutil
import zipfile
import urllib.request
from argparse import Namespace
import tts as t
from cog import BasePredictor, Input, Path as CogPath


class Predictor(BasePredictor):

    async def predict(self,
        model_name: str = Input(
            description="RVC model.",
            default="Sponge"), 
        tts_text: str = Input(
            description="text to speech",
            default="Hello guys! Test text now.")
    ) -> CogPath:
        file = await t.tts(model_name, tts_text)
        print(f"[+] Cover generated at {file}")
        return CogPath(cover_path)