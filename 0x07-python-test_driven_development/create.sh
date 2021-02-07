#!/bin/bash
git add $1
git stage $1
pre = "File"
post = "added"
git commit -m "$pre $1 $post"
git push
