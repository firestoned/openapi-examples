# coding: utf-8

"""
    Example person and addressbook API

    An example API with more than one resource

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI

from addressbook.apis.addressbook_api import router as AddressbookApiRouter

app = FastAPI(
    title="Example person and addressbook API",
    description="An example API with more than one resource",
    version="1.0",
)

app.include_router(AddressbookApiRouter)