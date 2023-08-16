#!/usr/bin/env python3
''' module for task 11 '''


def schools_by_topic(mongo_collection, topic):
    '''Python function that returns the list of schools having a specific topic'''
    if mongo_collection is None:
        return []
    
    try:
        schools = mongo_collection.find({"topics": topic})
        return list(schools)
    except Exception as e:
        print("An error occurred:", str(e))
        return []

