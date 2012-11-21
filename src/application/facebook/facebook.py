"""
This module contains helper classes and methods
for the facebook integration module

.. module:: application.facebook.facebook

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

import facebooksdk as fb
import models

from flask import flash

class AlbumList(object):
    def __init__(self, token):
        """
        Given an an access token this class
        will get all albums for the object associated with the token
        (i.e. a page or a user)

        It will lazily construct an Album instance for each of
        the album ids returned
        """
        
        self.graph = fb.GraphAPI(token.access_token)
        albums_data = self.graph.get_connections('me', 'albums')['data']

        self.album_ids = {}
        self.album_names = {}
        for data in albums_data:
            self.album_ids[data['id']] = data
            self.album_names[data['name']] = data

    def get_albums_by_name(self, names):
        """
        Given a list of names this method will
        return album objects for each matching name.

        If a name is not found then it is silently ignored.

        This method returns a dictionary mapping name
        to Album object.
        """

        albums = {}
        for name in names:
            if name in self.album_names:
                if isinstance(self.album_names[name], Album):
                    albums[name] = self.album_names[name]
                else:
                    self.album_names[name] = Album(graph=self.graph,
                                                   album_data=self.album_names[name])
                    self.album_ids[self.album_names[name].me] = self.album_names[name]
                    albums[name] = self.album_names[name]
        return albums

    def get_albums_by_id(self, ids):
        """
        Given a list of ids this method will
        return album objects for each matching id.

        If an id is not found then it is silently ignored.

        This method returns a dictionary mapping id to
        Album object
        """

        albums = {}
        for album_id in ids:
            if album_id in self.album_ids:
                if isinstance(self.album_ids[album_id], Album):
                    albums[album_id] = self.album_ids[album_id]
                else:
                    self.album_ids[album_id] = Album(graph=self.graph,
                                                     album_data=self.album_ids[album_id])
                    self.album_names[self.album_ids[album_id].name] = self.album_ids[album_id]
                    albums[album_id] = self.album_ids[album_id]
        return albums
        

    def get_all_albums_by_id(self):
        """
        This method returns a dictionary of all
        albums with album ids as the keys
        """

        for album_id in self.album_ids:
            if not isinstance(self.album_ids[album_id], Album):
                self.album_ids[album_id] = Album(graph=self.graph,
                                                 album_data=self.album_ids[album_id])
                self.album_names[self.album_ids[album_id].name] = self.album_ids[album_id]

        return self.album_ids

    def get_all_albums_by_name(self):
        """
        This method returns a dictionary of all
        albums with album names as the keys
        """

        for name in self.album_names:
            if not isinstance(self.album_names[name], Album):
                self.album_names[name] = Album(graph=self.graph,
                                               album_data=self.album_names[name])
                self.album_ids[self.album_names[name].me] = self.album_names[name]

        return self.album_names
                
        
class Album(object):
    def __init__(self, graph=None, token=None, album_id=None, album_data=None):
        """
        Initializes a new Album object.

        If graph is provided then the graph object is saved to this
        instance.

        If the token is provided then the graph object for this token
        is created and saved to this instance.

        If both are none then an error is raised.

        If album_id is provided then the graph object is queried
        for the id and the album object populates itself with this data

        If album_data is provided then the graph object is populated
        with the data in the json derived object

        If both are None then an error is raised
        """

        if graph is None and token is None:
            raise TypeError("Either a graph object must be provided or a token must be provided")

        if graph is not None:
            self.graph = graph
        else:
            self.graph = fb.GraphAPI(token.access_token)

        if album_id is None and album_data is None:
            raise TypeError("Either an album id or a album data must be provided")

        if album_id is not None:
            album_data = self.graph.get_object(album_id)

        self.me = album_data['id']
        self.name = album_data['name']
        self.desc = album_data.get('description', None)
        self.count = album_data.get('count', 0)
        if 'cover_photo' in album_data:
            self.cover_photo = Photo(self.me, graph=self.graph, photo_id=album_data['cover_photo']).thumbnail
        else:
            self.cover_photo = None

    def get_model(self):
        query = models.AlbumModel.all()
        query.filter('me =', self.me)

        try:
            return  query.fetch(1)[0]
        except IndexError:
            cover_thumb = None
            if self.cover_photo is not None:
                cover_thumb = self.cover_photo

            entity = models.AlbumModel(me=self.me,
                                       name=self.name,
                                       desc=self.desc,
                                       cover_photo=cover_thumb)
            entity.put()
            return entity

class Photo(object):
    def __init__(self, album_id, graph=None, token=None, photo_id=None, photo_data=None):
        if graph is None and token is None:
            raise TypeError("Either a graph object must be provided or a token must be provided")

        if graph is not None:
            self.graph = graph
        else:
            self.graph = fb.GraphAPI(token.access_token)

        if photo_id is None and photo_data is None:
            raise TypeError("Either an album id or a album data must be provided")

        if photo_id is not None:
            photo_data = self.graph.get_object(photo_id)

        self.me = photo_data['id']
        self.name = photo_data.get('name', None)
        self.thumbnail = photo_data['picture']
        self.original = photo_data['images'][0]['source']
        self.album_id = album_id

    def get_model(self):
        query = models.PhotoModel.all()
        query.filter('me =', self.me)

        try:
            return query.fetch(1)[0]
        except IndexError:
            entity = models.PhotoModel(me=self.me,
                                       album_id=self.album_id,
                                       name=self.name,
                                       thumbnail=self.thumbnail,
                                       original=self.original)
            entity.put()
            return entity
            