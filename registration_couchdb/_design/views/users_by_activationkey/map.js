function(doc)
{
    if(doc.doc_type == 'User')
    {
        if(doc.activation_key)
        {
            emit(doc.activation_key, null);
        }
    }
}
