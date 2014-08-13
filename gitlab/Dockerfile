FROM sameersbn/gitlab:latest

ADD google_oauth_enabler.py /google_oauth_enabler.py
RUN chmod +x /google_oauth_enabler.py && /google_oauth_enabler.py && echo '/google_oauth_enabler.py' >> /.profile
