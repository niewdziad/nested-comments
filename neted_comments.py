def print_comments(comments, indent=0):
    if "value" in comments:
        print("->" + " " * indent + comments["value"])
        if "subcomments" in comments:
            for subcomment in comments["subcomments"]:
                print_comments(subcomment, indent + 3)

comments = {
    "value": "Thread opening",
    "subcomments": [
        { "value": "sub1", "subcomments": [] },
        {
            "value": "sub2",
            "subcomments": [
                {
                    "value": "sub3",
                    "subcomments": [{ "value": "subclosing", "subcomments": [] }]
                }
            ]
        },
        []
    ]
}

print_comments(comments)
