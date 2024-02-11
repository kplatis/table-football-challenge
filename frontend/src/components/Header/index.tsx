'use client'

import { Menu, Group, Center, Burger } from '@mantine/core'
import { useDisclosure } from '@mantine/hooks'
import classes from './Header.module.css'

const links = [
  {
    link: '#1',
    label: 'Games',
    links: [
      { link: '/games', label: 'List Games' },
      { link: '/games/create', label: 'Create new game' },
    ],
  },
  { link: '/overview', label: 'Overview' },
  {
    link: '#2',
    label: 'Teams',
    links: [
      { link: '/teams', label: 'List teams' },
      { link: '/teams/create', label: 'Create a new team' },
    ],
  },
]

export function Header() {
  const [opened, { toggle }] = useDisclosure(false)

  const items = links.map((link) => {
    const menuItems = link.links?.map((item) => (
      <Menu.Item key={item.link}>{item.label}</Menu.Item>
    ))

    if (menuItems) {
      return (
        <Menu
          key={link.label}
          trigger="hover"
          transitionProps={{ exitDuration: 0 }}
          withinPortal
        >
          <Menu.Target>
            <a
              href={link.link}
              className={classes.link}
              onClick={(event) => event.preventDefault()}
            >
              <Center>
                <span className={classes.linkLabel}>{link.label}</span>
              </Center>
            </a>
          </Menu.Target>
          <Menu.Dropdown>{menuItems}</Menu.Dropdown>
        </Menu>
      )
    }

    return (
      <a
        key={link.label}
        href={link.link}
        className={classes.link}
        onClick={(event) => event.preventDefault()}
      >
        {link.label}
      </a>
    )
  })

  return (
    <header className={classes.header}>
      <div className={classes.inner}>
        <div>Challenge</div>
        <Group gap={10} visibleFrom="sm">
          {items}
        </Group>
        <Burger opened={opened} onClick={toggle} size="sm" hiddenFrom="sm" />
      </div>
    </header>
  )
}
