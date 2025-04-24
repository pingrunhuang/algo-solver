# /usr/bin/python
# coding=utf-8

'''
535. Encode and Decode TinyURL

'''

class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        encodedURL = longUrl
        return encodedURL
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == '__main__':
    codec = Codec()
    enc_str=codec.encode("https://leetcode.com/problems/design-tinyurl")
    print(enc_str)