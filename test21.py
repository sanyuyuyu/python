#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date:   2022-08-18 21:04:35
# @Last Modified time: 2022-08-18 21:30:44
# article/models.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
