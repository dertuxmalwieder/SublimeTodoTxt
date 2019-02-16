import sublime
import sublime_plugin


class TodoTxtAutocomplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        pref = sublime.Region(locations[0] - 1, locations[0])
        pref = view.substr(pref)

        if pref == '@':
            regex = r'\s\@\S+'  # Todo item context
        elif pref == '+':
            regex = r'\s\+\S+'  # Todo item project
        else:
            return

        matches = view.find_all(regex)
        matches = {view.substr(x).lstrip() for x in matches}

        autocompletes = [[x] * 2 for x in matches]
        return (autocompletes, sublime.INHIBIT_WORD_COMPLETIONS
                | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
