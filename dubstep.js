function songDecoder(song){
    var dub = song.replace(/WUBWUBWUB|WUBWUB|WUB/g,' ');
    return dub.replace(/^\s+|\s+$/g, '');
}
console.log(songDecoder('AWUBWUBWUBBWUBWUBWUBC'));