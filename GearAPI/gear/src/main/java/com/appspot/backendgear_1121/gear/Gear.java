/*
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */
/*
 * This code was generated by https://code.google.com/p/google-apis-client-generator/
 * (build: 2015-08-03 17:34:38 UTC)
 * on 2015-11-11 at 16:02:16 UTC 
 * Modify at your own risk.
 */

package com.appspot.backendgear_1121.gear;

/**
 * Service definition for Gear (v2).
 *
 * <p>
 * GearBackend API v1.
 * </p>
 *
 * <p>
 * For more information about this service, see the
 * <a href="" target="_blank">API Documentation</a>
 * </p>
 *
 * <p>
 * This service uses {@link GearRequestInitializer} to initialize global parameters via its
 * {@link Builder}.
 * </p>
 *
 * @since 1.3
 * @author Google, Inc.
 */
@SuppressWarnings("javadoc")
public class Gear extends com.google.api.client.googleapis.services.json.AbstractGoogleJsonClient {

  // Note: Leave this static initializer at the top of the file.
  static {
    com.google.api.client.util.Preconditions.checkState(
        com.google.api.client.googleapis.GoogleUtils.MAJOR_VERSION == 1 &&
        com.google.api.client.googleapis.GoogleUtils.MINOR_VERSION >= 15,
        "You are currently running with version %s of google-api-client. " +
        "You need at least version 1.15 of google-api-client to run version " +
        "1.20.0 of the gear library.", com.google.api.client.googleapis.GoogleUtils.VERSION);
  }

  /**
   * The default encoded root URL of the service. This is determined when the library is generated
   * and normally should not be changed.
   *
   * @since 1.7
   */
  public static final String DEFAULT_ROOT_URL = "https://backendgear-1121.appspot.com/_ah/api/";

  /**
   * The default encoded service path of the service. This is determined when the library is
   * generated and normally should not be changed.
   *
   * @since 1.7
   */
  public static final String DEFAULT_SERVICE_PATH = "gear/v2/";

  /**
   * The default encoded base URL of the service. This is determined when the library is generated
   * and normally should not be changed.
   */
  public static final String DEFAULT_BASE_URL = DEFAULT_ROOT_URL + DEFAULT_SERVICE_PATH;

  /**
   * Constructor.
   *
   * <p>
   * Use {@link Builder} if you need to specify any of the optional parameters.
   * </p>
   *
   * @param transport HTTP transport, which should normally be:
   *        <ul>
   *        <li>Google App Engine:
   *        {@code com.google.api.client.extensions.appengine.http.UrlFetchTransport}</li>
   *        <li>Android: {@code newCompatibleTransport} from
   *        {@code com.google.api.client.extensions.android.http.AndroidHttp}</li>
   *        <li>Java: {@link com.google.api.client.googleapis.javanet.GoogleNetHttpTransport#newTrustedTransport()}
   *        </li>
   *        </ul>
   * @param jsonFactory JSON factory, which may be:
   *        <ul>
   *        <li>Jackson: {@code com.google.api.client.json.jackson2.JacksonFactory}</li>
   *        <li>Google GSON: {@code com.google.api.client.json.gson.GsonFactory}</li>
   *        <li>Android Honeycomb or higher:
   *        {@code com.google.api.client.extensions.android.json.AndroidJsonFactory}</li>
   *        </ul>
   * @param httpRequestInitializer HTTP request initializer or {@code null} for none
   * @since 1.7
   */
  public Gear(com.google.api.client.http.HttpTransport transport, com.google.api.client.json.JsonFactory jsonFactory,
      com.google.api.client.http.HttpRequestInitializer httpRequestInitializer) {
    this(new Builder(transport, jsonFactory, httpRequestInitializer));
  }

  /**
   * @param builder builder
   */
  Gear(Builder builder) {
    super(builder);
  }

  @Override
  protected void initialize(com.google.api.client.googleapis.services.AbstractGoogleClientRequest<?> httpClientRequest) throws java.io.IOException {
    super.initialize(httpClientRequest);
  }

  /**
   * An accessor for creating requests from the Gearapi collection.
   *
   * <p>The typical use is:</p>
   * <pre>
   *   {@code Gear gear = new Gear(...);}
   *   {@code Gear.Gearapi.List request = gear.gearapi().list(parameters ...)}
   * </pre>
   *
   * @return the resource collection
   */
  public Gearapi gearapi() {
    return new Gearapi();
  }

  /**
   * The "gearapi" collection of methods.
   */
  public class Gearapi {

    /**
     * Create a request for the method "gearapi.define".
     *
     * This request holds the parameters needed by the gear server.  After setting any optional
     * parameters, call the {@link Define#execute()} method to invoke the remote operation.
     *
     * @param content the {@link com.appspot.backendgear_1121.gear.model.GearBackendDefinition}
     * @return the request
     */
    public Define define(com.appspot.backendgear_1121.gear.model.GearBackendDefinition content) throws java.io.IOException {
      Define result = new Define(content);
      initialize(result);
      return result;
    }

    public class Define extends GearRequest<com.appspot.backendgear_1121.gear.model.GearBackendDefinition> {

      private static final String REST_PATH = "gearapi/multiply";

      /**
       * Create a request for the method "gearapi.define".
       *
       * This request holds the parameters needed by the the gear server.  After setting any optional
       * parameters, call the {@link Define#execute()} method to invoke the remote operation. <p> {@link
       * Define#initialize(com.google.api.client.googleapis.services.AbstractGoogleClientRequest)} must
       * be called to initialize this instance immediately after invoking the constructor. </p>
       *
       * @param content the {@link com.appspot.backendgear_1121.gear.model.GearBackendDefinition}
       * @since 1.13
       */
      protected Define(com.appspot.backendgear_1121.gear.model.GearBackendDefinition content) {
        super(Gear.this, "POST", REST_PATH, content, com.appspot.backendgear_1121.gear.model.GearBackendDefinition.class);
      }

      @Override
      public Define setAlt(java.lang.String alt) {
        return (Define) super.setAlt(alt);
      }

      @Override
      public Define setFields(java.lang.String fields) {
        return (Define) super.setFields(fields);
      }

      @Override
      public Define setKey(java.lang.String key) {
        return (Define) super.setKey(key);
      }

      @Override
      public Define setOauthToken(java.lang.String oauthToken) {
        return (Define) super.setOauthToken(oauthToken);
      }

      @Override
      public Define setPrettyPrint(java.lang.Boolean prettyPrint) {
        return (Define) super.setPrettyPrint(prettyPrint);
      }

      @Override
      public Define setQuotaUser(java.lang.String quotaUser) {
        return (Define) super.setQuotaUser(quotaUser);
      }

      @Override
      public Define setUserIp(java.lang.String userIp) {
        return (Define) super.setUserIp(userIp);
      }

      @Override
      public Define set(String parameterName, Object value) {
        return (Define) super.set(parameterName, value);
      }
    }

  }

  /**
   * An accessor for creating requests from the Stories collection.
   *
   * <p>The typical use is:</p>
   * <pre>
   *   {@code Gear gear = new Gear(...);}
   *   {@code Gear.Stories.List request = gear.stories().list(parameters ...)}
   * </pre>
   *
   * @return the resource collection
   */
  public Stories stories() {
    return new Stories();
  }

  /**
   * The "stories" collection of methods.
   */
  public class Stories {

    /**
     * Create a request for the method "stories.listStory".
     *
     * This request holds the parameters needed by the gear server.  After setting any optional
     * parameters, call the {@link ListStory#execute()} method to invoke the remote operation.
     *
     * @return the request
     */
    public ListStory listStory() throws java.io.IOException {
      ListStory result = new ListStory();
      initialize(result);
      return result;
    }

    public class ListStory extends GearRequest<com.appspot.backendgear_1121.gear.model.GearBackendStoriesCollection> {

      private static final String REST_PATH = "recommendedstory";

      /**
       * Create a request for the method "stories.listStory".
       *
       * This request holds the parameters needed by the the gear server.  After setting any optional
       * parameters, call the {@link ListStory#execute()} method to invoke the remote operation. <p>
       * {@link
       * ListStory#initialize(com.google.api.client.googleapis.services.AbstractGoogleClientRequest)}
       * must be called to initialize this instance immediately after invoking the constructor. </p>
       *
       * @since 1.13
       */
      protected ListStory() {
        super(Gear.this, "GET", REST_PATH, null, com.appspot.backendgear_1121.gear.model.GearBackendStoriesCollection.class);
      }

      @Override
      public com.google.api.client.http.HttpResponse executeUsingHead() throws java.io.IOException {
        return super.executeUsingHead();
      }

      @Override
      public com.google.api.client.http.HttpRequest buildHttpRequestUsingHead() throws java.io.IOException {
        return super.buildHttpRequestUsingHead();
      }

      @Override
      public ListStory setAlt(java.lang.String alt) {
        return (ListStory) super.setAlt(alt);
      }

      @Override
      public ListStory setFields(java.lang.String fields) {
        return (ListStory) super.setFields(fields);
      }

      @Override
      public ListStory setKey(java.lang.String key) {
        return (ListStory) super.setKey(key);
      }

      @Override
      public ListStory setOauthToken(java.lang.String oauthToken) {
        return (ListStory) super.setOauthToken(oauthToken);
      }

      @Override
      public ListStory setPrettyPrint(java.lang.Boolean prettyPrint) {
        return (ListStory) super.setPrettyPrint(prettyPrint);
      }

      @Override
      public ListStory setQuotaUser(java.lang.String quotaUser) {
        return (ListStory) super.setQuotaUser(quotaUser);
      }

      @Override
      public ListStory setUserIp(java.lang.String userIp) {
        return (ListStory) super.setUserIp(userIp);
      }

      @Override
      public ListStory set(String parameterName, Object value) {
        return (ListStory) super.set(parameterName, value);
      }
    }

  }

  /**
   * Builder for {@link Gear}.
   *
   * <p>
   * Implementation is not thread-safe.
   * </p>
   *
   * @since 1.3.0
   */
  public static final class Builder extends com.google.api.client.googleapis.services.json.AbstractGoogleJsonClient.Builder {

    /**
     * Returns an instance of a new builder.
     *
     * @param transport HTTP transport, which should normally be:
     *        <ul>
     *        <li>Google App Engine:
     *        {@code com.google.api.client.extensions.appengine.http.UrlFetchTransport}</li>
     *        <li>Android: {@code newCompatibleTransport} from
     *        {@code com.google.api.client.extensions.android.http.AndroidHttp}</li>
     *        <li>Java: {@link com.google.api.client.googleapis.javanet.GoogleNetHttpTransport#newTrustedTransport()}
     *        </li>
     *        </ul>
     * @param jsonFactory JSON factory, which may be:
     *        <ul>
     *        <li>Jackson: {@code com.google.api.client.json.jackson2.JacksonFactory}</li>
     *        <li>Google GSON: {@code com.google.api.client.json.gson.GsonFactory}</li>
     *        <li>Android Honeycomb or higher:
     *        {@code com.google.api.client.extensions.android.json.AndroidJsonFactory}</li>
     *        </ul>
     * @param httpRequestInitializer HTTP request initializer or {@code null} for none
     * @since 1.7
     */
    public Builder(com.google.api.client.http.HttpTransport transport, com.google.api.client.json.JsonFactory jsonFactory,
        com.google.api.client.http.HttpRequestInitializer httpRequestInitializer) {
      super(
          transport,
          jsonFactory,
          DEFAULT_ROOT_URL,
          DEFAULT_SERVICE_PATH,
          httpRequestInitializer,
          false);
    }

    /** Builds a new instance of {@link Gear}. */
    @Override
    public Gear build() {
      return new Gear(this);
    }

    @Override
    public Builder setRootUrl(String rootUrl) {
      return (Builder) super.setRootUrl(rootUrl);
    }

    @Override
    public Builder setServicePath(String servicePath) {
      return (Builder) super.setServicePath(servicePath);
    }

    @Override
    public Builder setHttpRequestInitializer(com.google.api.client.http.HttpRequestInitializer httpRequestInitializer) {
      return (Builder) super.setHttpRequestInitializer(httpRequestInitializer);
    }

    @Override
    public Builder setApplicationName(String applicationName) {
      return (Builder) super.setApplicationName(applicationName);
    }

    @Override
    public Builder setSuppressPatternChecks(boolean suppressPatternChecks) {
      return (Builder) super.setSuppressPatternChecks(suppressPatternChecks);
    }

    @Override
    public Builder setSuppressRequiredParameterChecks(boolean suppressRequiredParameterChecks) {
      return (Builder) super.setSuppressRequiredParameterChecks(suppressRequiredParameterChecks);
    }

    @Override
    public Builder setSuppressAllChecks(boolean suppressAllChecks) {
      return (Builder) super.setSuppressAllChecks(suppressAllChecks);
    }

    /**
     * Set the {@link GearRequestInitializer}.
     *
     * @since 1.12
     */
    public Builder setGearRequestInitializer(
        GearRequestInitializer gearRequestInitializer) {
      return (Builder) super.setGoogleClientRequestInitializer(gearRequestInitializer);
    }

    @Override
    public Builder setGoogleClientRequestInitializer(
        com.google.api.client.googleapis.services.GoogleClientRequestInitializer googleClientRequestInitializer) {
      return (Builder) super.setGoogleClientRequestInitializer(googleClientRequestInitializer);
    }
  }
}