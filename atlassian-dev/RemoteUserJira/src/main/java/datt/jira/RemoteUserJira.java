package datt.jira;

import org.apache.log4j.Category;
import java.security.Principal;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.atlassian.jira.security.login.JiraSeraphAuthenticator;

public class RemoteUserJira extends JiraSeraphAuthenticator {
  private static final Category log = Category.getInstance(RemoteUserJira.class);

  public Principal getUser(HttpServletRequest request, HttpServletResponse response) {
    Principal user = null;
    try {
      if(request.getSession() != null && request.getSession().getAttribute(JiraSeraphAuthenticator.LOGGED_IN_KEY) != null) {
        log.debug("Session found; user already logged in");
        user = (Principal) request.getSession().getAttribute(JiraSeraphAuthenticator.LOGGED_IN_KEY);
      } else {
        log.debug("Looking for user header using RemoteUserJira for SSO");

        String remoteuser = request.getHeader("user");
        log.debug("user set to: " + remoteuser);

        if(remoteuser != null) {
          user = getUser(remoteuser);
          log.debug("Logging in with username: " + user);
          request.getSession().setAttribute(JiraSeraphAuthenticator.LOGGED_IN_KEY, user);
          request.getSession().setAttribute(JiraSeraphAuthenticator.LOGGED_OUT_KEY, null);
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
