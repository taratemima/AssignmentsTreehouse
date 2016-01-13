
package com.teamtreehouse.model;
public class SongRequest {
    private String mSinger;
    private Song mSong;

    public SongRequest(String singer, Song requestedSong) {
        mSinger = singer;
        mSong = requestedSong;
    }

    public String getSinger() {
        return mSinger;
    }

    public void setSinger(String singer) {
        mSinger = singer;
    }

    public Song getSong() {
        return mSong;
    }

    public void setSong(Song song) {
        mSong = song;
    }

    @Override
    public String toString() {
        return "SongRequest{" +
                "mSinger='" + mSinger + '\'' +
                ", mSong=" + mSong +
                '}';
    }
}

