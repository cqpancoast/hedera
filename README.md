# hedera

Complex to-do lists for the easily distracted.

Abstracts the idea of a todo list into “task graphs”, node-edge dependency structures.
Uses stripping ivy (genus Hedera) as a metaphor for accomplishing tasks — task graphs are here called “vines”, nodes are “tasks”, directed edges show dependency between tasks.
A vine is stored using a language-agnostic serialization, then loaded in a “session” into the language of some scripting API.
Because of serialization, both the API and the interface can be switched out between sessions. Tasks can have dictionary-style tags applied to them for use by the vanilla interface and by external tag-based plugins.
These provide additional functionality to an interface by making use of an API.

## Desired Functionality

This is also an ordered todo list.

- Serialization to allow the notion of a session and to promote imp-language-agnosticism
  - Tasks in a vine can connect to tasks on other vines with a URI to a tree and a node name on that tree.
- Scripting language API (Python first, the best language)
  - (I can learn how to code in different languages this way!)
  - Indivdual tasks are easy to reference
    - Tasks have a one-word name and then a brief git-commit-style description.
      - This promotes the good practice of creating sub-tasks if the original task isn’t clear from the short description.
- Projects and directory structures
  - There is no notion of a project, just a collection of seralized vines in the same directory.
  - One of the functions of an interface is to manage changing URI’s.
    - ivy add / ivy mv? I’d prefer to not do this, but I think it may be the only way to manage multiple serialized files.
- Command line interface, easy creation of other interfaces
  - Use of an API makes use of other interfaces easy
  - ivy do this, ivy do that…
  - Note that a session/serialization model requires a notion of saving
    - Maybe we can take advantage of this to only save valid vines, solving the “connected vine” problem
  - Notion of activation doesn’t preclude dealing with multiple vines simultaneously
    - Potentially from different projects, if there’s a notion of a project.
- Plugins
  - A plugin, by definition (at least mine), interacts with both the interface (such as the command line) and the API (such as Python), but, if possible, I’d like to codify that a plugin’s internals are as separate from the API and interface as possible.

