package datt.confluence;

import org.apache.log4j.Category;
import java.security.Principal;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.atlassian.confluence.user.ConfluenceAuthenticator;

public class RemoteUserConfluence extends ConfluenceAuthenticator {
  private static final Category log = Category.getInstance(RemoteUserConfluence.class);

  public Principal getUser(HttpServletRequest request, HttpServletResponse response) {
    Principal user = null;
    try {
      if(request.getSession() != null && request.getSession().getAttribute(ConfluenceAuthenticator.LOGGED_IN_KEY) != null) {
        log.debug("Session found; user already logged in");
        user = (Principal) request.getSession().getAttribute(ConfluenceAuthenticator.LOGGED_IN_KEY);
      } else {
        log.debug("Looking for user header using RemoteUserConfluence for SSO");

        String remoteuser = request.getHeader("user");
        log.debug("user set to: " + remoteuser);

        if(remoteuser != null) {
          user = getUser(remoteuser);
          log.debug("Logging in with username: " + user);
          request.getSession().setAttribute(ConfluenceAuthenticator.LOGGED_IN_KEY, user);
          request.getSession().setAttribute(ConfluenceAuthenticator.LOGGED_OUT_KEY, null);
        } else {
          log.warn("user is null");
          return null;
        }
      }
    } catch (Exception e) {
      log.warn("Exception: " + e, e);
    }
    return user;
  }
}
