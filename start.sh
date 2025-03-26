#!/bin/bash
export $(cat backend/.env | xargs)
uvicorn backend.main:app --reload
