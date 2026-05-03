from bson import ObjectId

def serialize_doc(doc):
    doc['id']=str(doc['id'])
    del doc['id']
    return doc