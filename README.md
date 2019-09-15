
# opengl-api-registry-reader

A simple tool for extracting information from the OpenGL API Registry.

INSERT MORE DETAILS HERE

The registry is currently located on github in the KhronosGroup organization:
https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master/xml/gl.xml

## Usage

Some example using command line and the api.

## Registry Info Details

The registry is simply a huge xml file containing information about enums
and functions.

The skeleton structure

```xml
<registry>
    <!-- GL type definitions. -->
    <types>
        <type>typedef unsigned int <name>GLenum</name>;</type>
        <type>typedef unsigned char <name>GLboolean</name>;</type>
        ...
    </types>

    <!-- An attempt to group enums together (not critical information) -->
    <groups>
        <group name="CullFaceMode">
            <enum name="GL_BACK"/>
            <enum name="GL_FRONT"/>
            <enum name="GL_FRONT_AND_BACK"/>
        </group>
        ...
    </groups>

    <!-- Multiple enums blocks with the enum names and values. Can point to a group -->    <enums namespace="GL" group="ContextProfileMask" type="bitmask">
        <enum value="0x00000001" name="GL_CONTEXT_CORE_PROFILE_BIT"/>
        <enum value="0x00000002" name="GL_CONTEXT_COMPATIBILITY_PROFILE_BIT"/>
    </enums>
    ...

    <!-- Details information about every GL function -->
    <commands namespace="GL">
        <command>
            <proto>void <name>glDrawArrays</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <glx type="render" opcode="193"/>
        </command>
        ...
    </command>

    <!-- Multiple feature blocks for each opengl version.
         These include the required and remove section
         referencing command names and enum names.

         Only including parts of GL 3.2 as it shows removal.
    -->
    <feature api="gl" name="GL_VERSION_1_1" number="1.1">...</feature>
    <feature api="gl" name="GL_VERSION_1_2" number="1.2">...</feature>
    <feature api="gl" name="GL_VERSION_1_3" number="1.3">...</feature>
    <feature api="gl" name="GL_VERSION_1_4" number="1.4">...</feature>
    <feature api="gl" name="GL_VERSION_1_5" number="1.5">...</feature>
    <feature api="gl" name="GL_VERSION_2_0" number="2.0">...</feature>
    <feature api="gl" name="GL_VERSION_2_1" number="2.1">...</feature>
    <feature api="gl" name="GL_VERSION_3_0" number="3.0">...</feature>
    <feature api="gl" name="GL_VERSION_3_1" number="3.1">...</feature>
    <feature api="gl" name="GL_VERSION_3_2" number="3.2">
        <require>
            <enum name="GL_CONTEXT_CORE_PROFILE_BIT"/>
            <enum name="GL_CONTEXT_COMPATIBILITY_PROFILE_BIT"/>
            <enum name="GL_LINES_ADJACENCY"/>
            <enum name="GL_LINE_STRIP_ADJACENCY"/>
            ...
        </require>
        <require comment="Reuse ARB_draw_elements_base_vertex">
            <command name="glDrawElementsBaseVertex"/>
            <command name="glDrawRangeElementsBaseVertex"/>
            <command name="glDrawElementsInstancedBaseVertex"/>
            <command name="glMultiDrawElementsBaseVertex"/>
        </require>
        <remove profile="core" comment="Compatibility-only GL 1.0 features removed from GL 3.2">
            <command name="glNewList"/>
            <command name="glEndList"/>
            <command name="glCallList"/>
            <command name="glCallLists"/>
            <command name="glDeleteLists"/>
            ...
        </remove>
        <remove profile="core" comment="Compatibility-only GL 1.1 features removed from GL 3.2">
            <enum name="GL_QUADS"/>
            <enum name="GL_POLYGON"/>
            ...
        </remove>
        ...
    </feature>
    <feature api="gl" name="GL_VERSION_3_3" number="3.3">...</feature>
    <feature api="gl" name="GL_VERSION_4_0" number="4.0">...</feature>
    <feature api="gl" name="GL_VERSION_4_1" number="4.1">...</feature>
    <feature api="gl" name="GL_VERSION_4_2" number="4.2">...</feature>
    <feature api="gl" name="GL_VERSION_4_3" number="4.3">...</feature>
    <feature api="gl" name="GL_VERSION_4_4" number="4.4">...</feature>
    <feature api="gl" name="GL_VERSION_4_5" number="4.5">...</feature>
    <feature api="gl" name="GL_VERSION_4_6" number="4.6">...</feature>
    <!-- There will also be feature blocks for gles -->

    <!-- Extension definitions are similar to features.
         The numer of extensions gathered here is staggering,
         but they can be filtered on the ``supported`` field
         to make it easier to handle.
    -->
    <extensions>
        <extension name="GL_EXT_debug_label" supported="gl|glcore|gles2">
            <require>
                <enum name="GL_PROGRAM_PIPELINE_OBJECT_EXT"/>
                <enum name="GL_PROGRAM_OBJECT_EXT"/>
                <enum name="GL_SHADER_OBJECT_EXT"/>
                <enum name="GL_BUFFER_OBJECT_EXT"/>
                <enum name="GL_QUERY_OBJECT_EXT"/>
                <enum name="GL_VERTEX_ARRAY_OBJECT_EXT"/>
                <command name="glLabelObjectEXT"/>
                <command name="glGetObjectLabelEXT"/>
            </require>
            <require comment="Depends on OpenGL ES 3.0">
                <enum name="GL_SAMPLER"/>
                <enum name="GL_TRANSFORM_FEEDBACK"/>
            </require>
        </extension>
        <extension name="GL_EXT_debug_marker" supported="gl|glcore|gles1|gles2">
            <require>
                <command name="glInsertEventMarkerEXT"/>
                <command name="glPushGroupMarkerEXT"/>
                <command name="glPopGroupMarkerEXT"/>
            </require>
        </extension>
        ...
    </extension>
</registry>
