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

package com.appspot.backendgear_1121.gear.model;

/**
 * Collection of stories
 *
 * <p> This is the Java data model class that specifies how to parse/serialize into the JSON that is
 * transmitted over HTTP when working with the gear. For a detailed explanation see:
 * <a href="http://code.google.com/p/google-http-java-client/wiki/JSON">http://code.google.com/p/google-http-java-client/wiki/JSON</a>
 * </p>
 *
 * @author Google, Inc.
 */
@SuppressWarnings("javadoc")
public final class GearBackendStoriesCollection extends com.google.api.client.json.GenericJson {

  /**
   * Recommendation that stores a story
   * The value may be {@code null}.
   */
  @com.google.api.client.util.Key
  private java.util.List<GearBackendRecommendedStory> items;

  static {
    // hack to force ProGuard to consider GearBackendRecommendedStory used, since otherwise it would be stripped out
    // see http://code.google.com/p/google-api-java-client/issues/detail?id=528
    com.google.api.client.util.Data.nullOf(GearBackendRecommendedStory.class);
  }

  /**
   * Recommendation that stores a story
   * @return value or {@code null} for none
   */
  public java.util.List<GearBackendRecommendedStory> getItems() {
    return items;
  }

  /**
   * Recommendation that stores a story
   * @param items items or {@code null} for none
   */
  public GearBackendStoriesCollection setItems(java.util.List<GearBackendRecommendedStory> items) {
    this.items = items;
    return this;
  }

  @Override
  public GearBackendStoriesCollection set(String fieldName, Object value) {
    return (GearBackendStoriesCollection) super.set(fieldName, value);
  }

  @Override
  public GearBackendStoriesCollection clone() {
    return (GearBackendStoriesCollection) super.clone();
  }

}
