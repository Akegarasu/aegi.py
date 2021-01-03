import os
import sys
import re


class Aegisub:
    def __init__(self, file_path: str):
        self.filePath = file_path
        # self.filePath = "1.ass"
        self.assFile: list = []
        self.scriptInfo: dict = {}
        self.projectGarbage: dict = {}
        self.stylesV4: list = []
        self.events: dict = {}

        self.read_ass()
        self.parse_script_info()
        self.parse_project_garbage()
        self.parse_styles()

    def read_ass(self):
        ass = []
        with open(self.filePath, 'r', encoding="utf-8") as fi:
            cache: list = fi.readlines()
        while "\n" in cache:
            ass.append(cache[:cache.index("\n")])
            cache = cache[cache.index("\n") + 1:]
        ass.append(cache)
        self.assFile = ass

    def parse_script_info(self):
        cache: dict = {}
        if "[Script Info]" in self.assFile[0][0]:
            script_info: list = self.assFile[0][3:]
        for eve in script_info:
            split_cache = eve.split(": ")
            cache[split_cache[0]] = split_cache[1].replace("\n", "")
        self.scriptInfo = cache

    def parse_project_garbage(self):
        cache: dict = {}
        if "[Aegisub Project Garbage]" in self.assFile[1][0]:
            project_garbage: list = self.assFile[1][1:]
        for eve in project_garbage:
            split_cache = eve.split(": ")
            cache[split_cache[0]] = split_cache[1].replace("\n", "")
        self.projectGarbage = cache

    def parse_styles(self):
        cache: list = []
        if "[V4+ Styles]" in self.assFile[2][0]:
            styles_format: list = self.assFile[2][1].split(": ")[1].split(", ")
            styles: list = self.assFile[2][2:]
        for eve in range(len(styles)):
            split_cache = styles[eve].split(": ")[1].split(",")
            cache_style: dict = {}
            for x in range(len(split_cache)):
                cache_style[styles_format[x].replace("\n", "")] = split_cache[x].replace("\n", "")
            cache.append(cache_style)
        self.stylesV4 = cache

if __name__ == "__main__":
    p = Aegisub("1.ass")
    print("run")
