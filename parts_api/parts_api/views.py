from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import sqlite3

connection = sqlite3.connect("db.sqlite3", check_same_thread=False)

def home(request):
    return render(request, "index.html")

@csrf_exempt
def update_part(request, part_id):
    part = {}

    if request.content_type == 'multipart/form-data':
        encoding = 'utf-8'
        decoded = request.body.decode(encoding)
        split_values = decoded.split('\n')
        split_keys = decoded.split('"')
        values = split_values[3::4]
        keys = split_keys[1::2]

        for i in range(len(keys)):
            part[keys[i]] = values[i].replace('\r', '')

        for x, y in part.items():
            if x == 'weight_ounces':
                part['weight_ounces'] = int(y)
            if x == 'is_active':
                part['is_active'] = int(y)
                
    elif request.content_type == 'application/json': 
        part = json.loads(request.body)

    if request.method == 'GET':
        try:
            c = connection.cursor()
            try:
                c.execute("SELECT * FROM part WHERE id = ?", part_id)
                row = c.fetchone()
                return render(request, "part.html", {'data': row})
            finally:
                c.close()
        except:
            return HttpResponse(status=500)

    if request.method == 'PUT':
        value_pairs = ",".join(
            (
                "{key}='{value}'".format(key=key, value=value)
                if isinstance(value, (str, bool))
                else "{key}={value}".format(key=key, value=value)
                for key, value in part.items()
            )
        )
        try:
            c = connection.cursor()
            try:
                c.execute(
                    "UPDATE part SET {value_pairs} WHERE id={part_id}".format(
                        value_pairs=value_pairs, part_id=part_id
                    )
                )
            finally:
                c.close()
        except:
            return HttpResponse(status=500)

    if request.method == 'POST':
        value_pairs = ",".join(
            (
                "{value}".format(key=key, value=value)
                if isinstance(value, (str, bool))
                else "{value}".format(key=key, value=value)
                for key, value in part.items()
            )
        )
        try:
            arr = value_pairs.split(',')

            if arr[4] == 'False':
                arr[4] = 0
            elif arr[4] == 'True':
                arr[4] = 1

            c = connection.cursor()
            try:
                c.execute("INSERT INTO part (name, sku, description, weight_ounces, is_active) VALUES (?, ?, ?, ?, ?)", [arr[0], arr[1], arr[2], arr[3], arr[4]])
            finally:
                c.close()
        except:
            return HttpResponse(status=500)

    if request.method == 'DELETE':
        try:
            c = connection.cursor()
            try:
                c.execute("DELETE FROM part WHERE id = ?", part_id)
            finally:
                c.close()
        except:
            return HttpResponse(status=500)

    return HttpResponse(status=200)

def mostCommon(input):
    words = input.split(' ')

    # Get the set of unique words.
    uniques = []
    for word in words:
        if word not in uniques:
            uniques.append(word)

    # Make a list of (count, unique) tuples.
    counts = []
    for unique in uniques:
        count = 0              # Initialize the count to zero.
        for word in words:     # Iterate over the words.
            if word == unique:   # Is this word equal to the current unique?
                count += 1         # If so, increment the count
        counts.append((count, unique))

    five = {}
    counts.sort()            # Sorting the list puts the lowest counts first.
    counts.reverse()         # Reverse it, putting the highest counts first.
    # Print the ten words with the highest counts.
    for i in range(min(5, len(counts))):
        count, word = counts[i]
        print('%s %d' % (word, count))
        five[word] = count
    return five